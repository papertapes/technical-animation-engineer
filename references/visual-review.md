# Visual Review Protocol

Code review cannot see overlaps, broken arrows, or a caption lagging one
step behind the picture. Visual review = screenshots + judgment.

## 1. Capture protocol

For each animation, capture:

| Shot | When | Why |
|---|---|---|
| initial | `t=0`, before play | first impression, legend, initial state correct |
| early / mid / late | distinctive moments (per storyboard) | progression, mid-state layout |
| exception | during the exception scenario | error styling, recovery path visible |
| final | end of story | end state |
| narrow | any of the above at ~720 px width | responsive behavior |

Also: both themes (light/dark) at least once per page. Save shots to
`tests/browser-tests/screenshots/<page>/<shot>.png` (or alongside a
standalone audit) and reference them in the validation report.

## 2. Review checklist (per shot)

- [ ] No text overflow / truncation / clipped labels
- [ ] No unintended overlaps; z-order sensible
- [ ] Arrow directions match the described flow (marker orientation correct)
- [ ] Alignment: elements on a coherent grid; consistent spacing
- [ ] Color semantics consistent (data vs control vs error vs active —
      same meaning as the rest of the project)
- [ ] Contrast readable (both themes; dark theme especially)
- [ ] Caption text matches the visible state (sync check!)
- [ ] Pace readable: could a learner follow this at 1×?
- [ ] Nothing animated that carries no information (coherence)
- [ ] Typography: no over-bolding, hierarchy by size/weight *within reason*

## 3. Cross-frame checks (flip between shots)

- State changes are *visible* where the storyboard says they are
  (highlight actually moved, counter actually incremented).
- Objects persist where they should; nothing pops in/out without cause.
- The stage composition stays stable (no layout jumps between steps).

## 4. Judgment scale

- **Blocker** — misleading picture (arrow implies wrong direction, wrong
  object highlighted), unreadable text, broken layout.
- **Major** — desync, overlap that hides information, missing state change.
- **Minor** — spacing, alignment nits, tone/wording of captions.

Blockers/majors go back to implementation; re-review after fixes with fresh
screenshots.

## 6. Relation to the Visual Quality Gate

This file covers *defect review* (things broken). Expressiveness is a
separate, independent gate: the 10-question scored review and old-vs-new
comparison protocol live in [visual-quality-gate.md](visual-quality-gate.md).
For upgrade tasks, run both: defect review first (blockers/majors fixed),
then the quality gate (scores recorded, delta ≥ +5 to pass). The comparison
shot list (initial / 25% / 50% / 75% / end / exception / narrow) extends §1
above — capture the **same list for old and new versions**.

## 5. Who reviews

A reviewer that didn't write the code (another person, another agent pass)
is strongly preferred — familiarity breeds blindness. Record reviewer
identity and shot paths in the validation report. Claim only what the
screenshots show.
