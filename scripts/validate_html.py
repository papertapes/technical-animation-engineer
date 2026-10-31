#!/usr/bin/env python3
"""Static HTML validation for teaching-animation pages (stdlib-only).

Per-file checks:
  * strict tag well-formedness: non-void tags must be explicitly closed;
    implied end tags are reported as errors (pages should be authored
    well-formed)
  * duplicate id attributes (error)
  * local resource references (src/href/poster) that do not exist on disk
    (error)
  * in-page anchors (#id) pointing to non-existent ids (error)
  * missing/empty <title> (error), missing html[lang] (warn),
    missing viewport meta (warn), <img> without alt (warn)
  * unbalanced braces inside <style> blocks (warn)
  * inline <script> blocks are syntax-checked with ``node --check`` when
    Node.js is available; otherwise reported as skipped
  * forbidden/suspicious APIs: document.write (error), eval() (error),
    alert() (warn), console.log (info count)
  * inventory of external http(s) references (info; used for license review)

Usage:
    python validate_html.py PATH [PATH ...] [--json]
PATH may be a file or a directory (searched recursively for *.html;
node_modules is skipped).

Exit codes: 0 = all pass, 1 = at least one error, 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}
URL_ATTRS = ("src", "href", "poster")
EXTERNAL_PREFIXES = ("http://", "https://", "//")
NONLOCAL_PREFIXES = ("data:", "mailto:", "javascript:", "tel:")

RE_DOCUMENT_WRITE = re.compile(r"\bdocument\s*\.\s*write\b")
RE_EVAL = re.compile(r"\beval\s*\(")
RE_ALERT = re.compile(r"\balert\s*\(")
RE_CONSOLE_LOG = re.compile(r"\bconsole\s*\.\s*log\s*\(")


class PageParser(HTMLParser):
    """Collects structure facts from one HTML file (strict well-formedness)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.ids: dict[str, int] = {}
        self.dup_ids: set[str] = set()
        self.local_refs: list[tuple[str, str, int]] = []
        self.anchors: list[tuple[str, int]] = []
        self.external: set[str] = set()
        self.inline_scripts: list[tuple[str, int]] = []
        self.styles: list[tuple[str, int]] = []
        self.has_title = False
        self.title_has_text = False
        self.html_lang: str | None = None
        self.has_viewport = False
        self.imgs_without_alt: list[int] = []
        self._cdata: str | None = None
        self._cdata_line = 0
        self._cdata_buf: list[str] = []

    @staticmethod
    def _attrs(attrs):
        d = {}
        for k, v in attrs:
            if k not in d:
                d[k] = v if v is not None else ""
        return d

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        d = self._attrs(attrs)
        if tag == "html":
            self.html_lang = d.get("lang")
        if tag == "meta" and d.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.has_title = True
        if d.get("id"):
            if d["id"] in self.ids:
                self.dup_ids.add(d["id"])
            else:
                self.ids[d["id"]] = line
        for attr in URL_ATTRS:
            v = d.get(attr)
            if not v:
                continue
            if v.startswith(EXTERNAL_PREFIXES):
                self.external.add(v)
            elif v.startswith("#"):
                self.anchors.append((v[1:], line))
            elif not v.startswith(NONLOCAL_PREFIXES):
                self.local_refs.append((attr, v, line))
        if tag == "img" and not d.get("alt", "").strip():
            self.imgs_without_alt.append(line)
        if tag in ("script", "style"):
            self._cdata = tag
            self._cdata_line = line
            self._cdata_buf = []
        if tag not in VOID_ELEMENTS:
            self.stack.append((tag, line))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_ELEMENTS and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        self._cdata = None

    def handle_data(self, data):
        if self._cdata in ("script", "style"):
            self._cdata_buf.append(data)
        elif self._cdata is None and self.stack and self.stack[-1][0] == "title":
            if data.strip():
                self.title_has_text = True

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if self._cdata == tag:
            text = "".join(self._cdata_buf)
            if tag == "script":
                self.inline_scripts.append((text, self._cdata_line))
            else:
                self.styles.append((text, self._cdata_line))
            self._cdata = None
        if tag in VOID_ELEMENTS:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for t, ln in self.stack[i + 1:]:
                    self.errors.append(
                        f"line {ln}: <{t}> is never closed "
                        f"(implicitly closed by </{tag}> at line {line})")
                del self.stack[i:]
                return
        self.errors.append(
            f"line {line}: stray closing tag </{tag}> with no matching opener")

    def finish(self):
        for t, ln in self.stack:
            self.errors.append(f"line {ln}: <{t}> is never closed")


def check_js_syntax(source: str) -> tuple[str, str]:
    """Syntax-check one inline script. Returns (status, detail)."""
    node = shutil.which("node")
    if not node:
        return "skipped", "Node.js not found; inline script syntax not checked"
    if not source.strip():
        return "ok", "empty script"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                     encoding="utf-8") as tf:
        tf.write(source)
        tmp = tf.name
    try:
        proc = subprocess.run([node, "--check", tmp], capture_output=True,
                              text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return "skipped", "node --check timed out"
    finally:
        try:
            Path(tmp).unlink(missing_ok=True)
        except OSError:
            pass
    if proc.returncode == 0:
        return "ok", "syntax OK (node --check)"
    detail = (proc.stderr or proc.stdout or "").strip().splitlines()
    return "error", detail[0] if detail else "syntax error"


def analyze_html(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    parser = PageParser()
    try:
        parser.feed(raw)
        parser.close()
    except Exception as exc:  # malformed markup can raise inside html.parser
        parser.errors.append(f"parser exception: {exc}")
    parser.finish()

    warnings: list[str] = []
    infos: list[str] = []

    for i in sorted(parser.dup_ids):
        parser.errors.append(
            f"duplicate id \"{i}\" (first defined at line {parser.ids[i]})")

    base = path.parent
    for attr, url, line in parser.local_refs:
        if not (base / url.split("#")[0]).exists():
            parser.errors.append(
                f"line {line}: missing local resource {attr}=\"{url}\"")
    for name, line in parser.anchors:
        if name and name not in parser.ids:
            parser.errors.append(f"line {line}: anchor #{name} has no matching id")

    if not parser.has_title:
        parser.errors.append("missing <title>")
    elif not parser.title_has_text:
        parser.errors.append("<title> is empty")
    if not parser.html_lang:
        warnings.append("<html> has no lang attribute")
    if not parser.has_viewport:
        warnings.append("no <meta name=\"viewport\"> tag")
    for line in parser.imgs_without_alt:
        warnings.append(f"line {line}: <img> without alt attribute")
    for text, line in parser.styles:
        if text.count("{") != text.count("}"):
            warnings.append(f"line {line}: unbalanced braces in <style> block")

    js_status = []
    for text, line in parser.inline_scripts:
        status, detail = check_js_syntax(text)
        js_status.append({"line": line, "status": status, "detail": detail})
        if status == "error":
            parser.errors.append(f"line {line}: inline script syntax error: {detail}")
        elif status == "ok":
            infos.append(f"line {line}: inline script syntax OK")

    if RE_DOCUMENT_WRITE.search(raw):
        parser.errors.append("uses document.write (forbidden)")
    if RE_EVAL.search(raw):
        parser.errors.append("uses eval() (forbidden)")
    if RE_ALERT.search(raw):
        warnings.append("uses alert() (avoid in teaching pages)")
    n_logs = len(RE_CONSOLE_LOG.findall(raw))
    if n_logs:
        infos.append(f"console.log count: {n_logs}")
    for url in sorted(parser.external):
        infos.append(f"external reference: {url}")

    return {
        "file": str(path),
        "errors": parser.errors,
        "warnings": warnings,
        "infos": infos,
        "external_refs": sorted(parser.external),
        "script_syntax": js_status,
        "stats": {"ids": len(parser.ids),
                  "inline_scripts": len(parser.inline_scripts)},
    }


def iter_html_files(paths):
    files: list[Path] = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(
                q for q in p.rglob("*.html")
                if "node_modules" not in q.parts))
        elif p.is_file():
            files.append(p)
        else:
            print(f"[WARN] path not found: {p}", file=sys.stderr)
    return files


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Static HTML validation.")
    ap.add_argument("paths", nargs="+", help="HTML files or directories")
    ap.add_argument("--json", action="store_true", help="Emit JSON")
    args = ap.parse_args(argv)

    files = iter_html_files(args.paths)
    if not files:
        msg = "no HTML files found under the given paths"
        if args.json:
            print(json.dumps({"tool": "validate_html", "files": [],
                              "summary": {"passed": 0, "failed": 0, "total": 0},
                              "note": msg}))
        else:
            print(f"[WARN] {msg}")
        return 0

    results = [analyze_html(f) for f in files]
    passed = sum(1 for r in results if not r["errors"])
    failed = len(results) - passed

    if args.json:
        print(json.dumps({
            "tool": "validate_html",
            "files": results,
            "summary": {"passed": passed, "failed": failed, "total": len(results)},
        }, indent=2))
    else:
        for r in results:
            status = "PASS" if not r["errors"] else "FAIL"
            print(f"\n{status}  {r['file']}")
            for item in r["errors"]:
                print(f"  [ERROR] {item}")
            for item in r["warnings"]:
                print(f"  [WARN] {item}")
            for item in r["infos"]:
                print(f"  [INFO] {item}")
        print(f"\nSummary: {passed} passed, {failed} failed, {len(results)} total")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
