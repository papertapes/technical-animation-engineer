#!/usr/bin/env python3
"""Contract validator for interactive teaching animations.

Animations built with this skill follow the unified control contract
documented in ``references/timeline-control.md``.

REQUIRED (error if missing):
  - play/pause control: element with data-tae-action="play-pause"
    (or separate "play" and "pause" actions)
  - reset control: data-tae-action="reset"

RECOMMENDED (warn if missing):
  - step controls: data-tae-action="step-fwd" / "step-back"
  - speed control: data-tae-action="speed"
  - timeline scrubber: data-tae-timeline
  - caption element: data-tae-caption (or class tae-caption)
  - evidence tags naming the technical basis (SPEC / VENDOR / TEACHING / ...)
  - window.__TAE__ or window.tae state API for tests and debugging
  - prefers-reduced-motion media query

ANTI-PATTERNS:
  - more than one setInterval() (error): a page must have one timing source
  - alert() / eval() / document.write (error)
  - inline onclick= handlers (warn; addEventListener recommended)
  - setInterval() used but no requestAnimationFrame() (info)

Also re-runs the base HTML checks from validate_html.py.

Usage:
    python validate_animation.py PATH [PATH ...] [--json]

Exit codes: 0 = pass, 1 = errors, 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_html import analyze_html, iter_html_files  # noqa: E402

RE_ACTION = re.compile(r'data-tae-action="([a-z0-9-]+)"')
RE_BUTTON = re.compile(r"<button\b[^>]*>.*?</button>", re.S | re.I)
RE_ONCLICK = re.compile(r"\sonclick\s*=")
RE_INTERVAL = re.compile(r"\bsetInterval\s*\(")
RE_RAF = re.compile(r"\brequestAnimationFrame\s*\(")
RE_STEP_ATTR = re.compile(r'data-tae-step="([^"]+)"')
RE_TAE_API = re.compile(r"window\s*\.\s*(?:__TAE__|tae)\b")
EVIDENCE_TAGS = ("SPEC", "VENDOR", "CHIP", "SDK", "TEACHING",
                 "VERIFIED", "UNVERIFIED")


def contract_checks(raw: str):
    errors: list[str] = []
    warnings: list[str] = []
    infos: list[str] = []

    actions = set(RE_ACTION.findall(raw))

    has_playpause = "play-pause" in actions or ("play" in actions and "pause" in actions)
    if not has_playpause:
        errors.append("missing play/pause control (data-tae-action=\"play-pause\")")
    else:
        infos.append("play/pause control present")
    if "reset" not in actions:
        errors.append("missing reset control (data-tae-action=\"reset\")")
    else:
        infos.append("reset control present")

    for rec, label in (("step-fwd", "step forward"),
                       ("step-back", "step backward"),
                       ("speed", "speed control")):
        if rec not in actions:
            warnings.append(f"recommended control missing: {label}")
    if "data-tae-timeline" not in raw:
        warnings.append("recommended: no timeline scrubber (data-tae-timeline)")
    if "data-tae-caption" not in raw and "tae-caption" not in raw:
        warnings.append("recommended: no caption element (data-tae-caption)")
    if not any(tag in raw for tag in EVIDENCE_TAGS):
        warnings.append(
            "recommended: no evidence tags (SPEC/VENDOR/TEACHING/VERIFIED...) in page")
    if not RE_TAE_API.search(raw):
        warnings.append("recommended: no window.__TAE__ state API")
    if "prefers-reduced-motion" not in raw:
        warnings.append("recommended: no prefers-reduced-motion handling")

    n_intervals = len(RE_INTERVAL.findall(raw))
    if n_intervals > 1:
        errors.append(
            f"{n_intervals} setInterval() calls found; a page must use one "
            "timing source (see references/timeline-control.md)")
    elif n_intervals == 1:
        warnings.append(
            "uses setInterval(); timestamp-driven requestAnimationFrame loop preferred")
    if n_intervals and not RE_RAF.search(raw):
        infos.append("no requestAnimationFrame() found")

    n_onclick = len(RE_ONCLICK.findall(raw))
    if n_onclick:
        warnings.append(
            f"{n_onclick} inline onclick= handler(s); prefer addEventListener")

    for pattern, msg in ((r"\balert\s*\(", "uses alert()"),
                         (r"\beval\s*\(", "uses eval()"),
                         (r"\bdocument\s*\.\s*write\b", "uses document.write")):
        if re.search(pattern, raw):
            errors.append(msg)

    steps = RE_STEP_ATTR.findall(raw)
    if len(steps) != len(set(steps)):
        errors.append("duplicate data-tae-step values")

    for btn in RE_BUTTON.findall(raw):
        has_label = re.search(r"aria-label(l?edby)?\s*=", btn)
        has_text = re.search(r">[^<]*\w", btn)
        if not has_label and not has_text:
            warnings.append("button without aria-label or visible text content")

    return errors, warnings, infos


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Animation contract validation.")
    ap.add_argument("paths", nargs="+", help="HTML files or directories")
    ap.add_argument("--json", action="store_true", help="Emit JSON")
    args = ap.parse_args(argv)

    files = iter_html_files(args.paths)
    if not files:
        msg = "no HTML files found under the given paths"
        if args.json:
            print(json.dumps({"tool": "validate_animation", "files": [],
                              "summary": {"passed": 0, "failed": 0, "total": 0},
                              "note": msg}))
        else:
            print(f"[WARN] {msg}")
        return 0

    results = []
    for f in files:
        base = analyze_html(f)
        raw = f.read_text(encoding="utf-8", errors="replace")
        c_errors, c_warnings, c_infos = contract_checks(raw)
        results.append({
            "file": str(f),
            "errors": base["errors"] + c_errors,
            "warnings": base["warnings"] + c_warnings,
            "infos": base["infos"] + c_infos,
        })

    passed = sum(1 for r in results if not r["errors"])
    failed = len(results) - passed

    if args.json:
        print(json.dumps({
            "tool": "validate_animation",
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
