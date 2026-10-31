#!/usr/bin/env python3
"""Structural validator for an Agent Skill directory (open Agent Skills layout).

Validates:
  1. SKILL.md exists and carries valid YAML frontmatter (subset parser).
  2. ``name``: lowercase letters/digits/hyphens, max 64 chars (open-spec rule).
  3. ``description``: non-empty, max 1024 chars, states trigger conditions.
  4. SKILL.md length guidance (warn above 500 lines; move detail to references/).
  5. references/, assets/, scripts/ exist; project template files present.
  6. Every Python script in scripts/ compiles.
  7. All relative markdown links inside skill .md files resolve on disk.
  8. Every file under references/ is mentioned in SKILL.md (orphan check).

stdlib-only (no third-party dependencies).

Exit codes: 0 = pass (warnings allowed), 1 = validation errors, 2 = usage error.

Usage:
    python validate_skill.py [SKILL_DIR] [--json]
"""
from __future__ import annotations

import argparse
import json
import py_compile
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
DESC_MAX = 1024          # open-spec limit for the description field
SKILL_LINE_WARN = 500    # best-practice warning threshold for SKILL.md length

# Project-specific layout expectations (applied only to this skill's directory).
PROJECT_EXPECTED = {
    "assets": [
        "storyboard-template.md",
        "animation-spec-template.md",
        "validation-report-template.md",
    ],
    "scripts": [
        "validate_skill.py",
        "validate_html.py",
        "validate_animation.py",
    ],
    "references": [
        "animation-taxonomy.md",
        "technical-accuracy.md",
        "storyboard-method.md",
        "svg-animation.md",
        "timeline-control.md",
        "visual-design.md",
        "interaction-design.md",
        "accessibility.md",
        "animation-testing.md",
        "visual-review.md",
    ],
}


def unquote(value: str) -> str:
    """Strip a single layer of matching single/double quotes."""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def parse_frontmatter(text: str):
    """Parse the YAML subset used by SKILL.md frontmatter.

    Supports: ``key: value`` scalars, quoted scalars, one level of nested
    maps, and ``>``/``|`` block scalars. Returns ``(meta, errors)``.
    """
    meta: dict = {}
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return meta, ["file does not start with a '---' frontmatter delimiter"]
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return meta, ["frontmatter is never closed with a second '---'"]

    fm = lines[1:end]
    i = 0
    current: str | None = None
    while i < len(fm):
        raw = fm[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
        if not m:
            errors.append(f"frontmatter line {i + 2}: cannot parse {stripped!r}")
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        indented = raw[:1] in (" ", "\t")
        if not indented:
            current = key
            if val == "":
                meta[key] = {}
            elif val in (">", "|", ">-", "|-"):
                block: list[str] = []
                j = i + 1
                while j < len(fm) and (fm[j][:1] in (" ", "\t") or not fm[j].strip()):
                    if fm[j].strip():
                        block.append(fm[j].strip())
                    j += 1
                meta[key] = " ".join(block)
                i = j
                continue
            else:
                meta[key] = unquote(val)
        elif indented and current is not None:
            if not isinstance(meta.get(current), dict):
                meta[current] = {}
            meta[current][key] = unquote(val)
        else:
            errors.append(f"frontmatter line {i + 2}: unexpected indented key {key!r}")
        i += 1
    return meta, errors


def validate(root: Path):
    errors: list[str] = []
    warnings: list[str] = []
    infos: list[str] = []

    skill = root / "SKILL.md"
    if not skill.is_file():
        errors.append("SKILL.md not found")
        return errors, warnings, infos

    text = skill.read_text(encoding="utf-8")
    meta, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    # ---- frontmatter field checks -------------------------------------
    name = meta.get("name")
    if not name:
        errors.append("frontmatter: missing required field 'name'")
    else:
        name = str(name)
        if not NAME_RE.match(name):
            errors.append(
                f"frontmatter: name {name!r} must be lowercase letters/digits "
                "separated by single hyphens")
        if len(name) > 64:
            errors.append(f"frontmatter: name exceeds 64 chars ({len(name)})")
        if name != root.name:
            warnings.append(
                f"frontmatter: name {name!r} does not match directory name {root.name!r}")

    desc = meta.get("description")
    if not desc:
        errors.append("frontmatter: missing required field 'description'")
    else:
        desc = str(desc)
        if len(desc) > DESC_MAX:
            errors.append(
                f"frontmatter: description is {len(desc)} chars (limit {DESC_MAX})")
        low = desc.lower()
        if not any(t in low for t in (
                "use when", "use this", "use for", "when the user",
                "when a user", "trigger")):
            warnings.append(
                "frontmatter: description should state when the skill should "
                "be used (trigger conditions)")
        if re.match(r"^\s*i\b", desc):
            warnings.append("frontmatter: description should be third person")

    license_field = meta.get("license")
    if not license_field:
        warnings.append("frontmatter: no 'license' field (recommended for public skills)")
    else:
        infos.append(f"frontmatter: license = {license_field}")

    # ---- length guidance ------------------------------------------------
    n_lines = len(text.splitlines())
    if n_lines > SKILL_LINE_WARN:
        warnings.append(
            f"SKILL.md has {n_lines} lines (guidance: keep under "
            f"{SKILL_LINE_WARN}; move detail to references/)")
    infos.append(f"SKILL.md: {n_lines} lines, {len(text.split())} words")

    # ---- layout ----------------------------------------------------------
    for sub in ("references", "assets", "scripts"):
        if not (root / sub).is_dir():
            warnings.append(f"missing conventional directory: {sub}/")
    expected = PROJECT_EXPECTED if root.name == "technical-animation-engineer" else {}
    for sub, files in expected.items():
        for f in files:
            if not (root / sub / f).is_file():
                warnings.append(f"missing project file: {sub}/{f}")

    # ---- scripts compile -------------------------------------------------
    sdir = root / "scripts"
    if sdir.is_dir():
        for py in sorted(sdir.glob("*.py")):
            try:
                py_compile.compile(str(py), doraise=True)
                infos.append(f"script compiles: scripts/{py.name}")
            except py_compile.PyCompileError as exc:
                errors.append(f"script does not compile: scripts/{py.name}: {exc}")

    # ---- relative markdown links resolve ---------------------------------
    md_files = [skill]
    if (root / "references").is_dir():
        md_files += sorted((root / "references").glob("*.md"))
    for md in md_files:
        base = md.parent
        for m in MD_LINK_RE.finditer(md.read_text(encoding="utf-8")):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path_part = target.split("#")[0]
            if not path_part:
                continue
            if not (base / path_part).exists():
                rel = md.relative_to(root) if md.is_relative_to(root) else md
                errors.append(f"{rel}: broken relative link -> {target}")

    # ---- orphan reference check -------------------------------------------
    if (root / "references").is_dir():
        for ref in sorted((root / "references").glob("*.md")):
            if ref.name not in text:
                warnings.append(
                    f"references/{ref.name} is never mentioned in SKILL.md "
                    "(orphan reference)")

    return errors, warnings, infos


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validate an Agent Skill directory.")
    ap.add_argument("skill_dir", nargs="?", default=".",
                    help="Path to the skill directory containing SKILL.md")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = ap.parse_args(argv)

    root = Path(args.skill_dir).resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    errors, warnings, infos = validate(root)
    passed = not errors
    result = {
        "tool": "validate_skill",
        "target": str(root),
        "errors": errors,
        "warnings": warnings,
        "infos": infos,
        "passed": passed,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Validating skill: {root}")
        for label, items in (("ERROR", errors), ("WARN", warnings), ("INFO", infos)):
            for item in items:
                print(f"[{label}] {item}")
        print(f"Result: {'PASS' if passed else 'FAIL'} "
              f"({len(errors)} errors, {len(warnings)} warnings)")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
