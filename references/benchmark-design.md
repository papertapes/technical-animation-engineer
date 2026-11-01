# Benchmark Design

Benchmarks are how the skill proves its own capability: designed examples,
built with the skill's full workflow, measured with the visual scoring
system, recorded honestly.

## 1. What a benchmark is

A benchmark is an independent, runnable HTML animation that (a) teaches a
real, spec-verified technical topic, (b) demonstrates a target visual level
with a deliberately chosen art direction, (c) exposes the full control
contract, and (d) is scored — not by effect counts, but by
[visual-scoring.md](../benchmarks/visual-scoring.md).

## 2. Design requirements (before code)

- **Art direction**: ≥ 3 distinct directions proposed per
  [art-direction.md](art-direction.md); selection recorded with reasons.
- **Storyboard**: scene sheet per [visual-storytelling.md](visual-storytelling.md)
  with composition, camera, motion, interactions per scene.
- **Technical basis**: every fact tagged and sourced (§-level citations from
  the official standard; USB facts verified against the USB-IF document).
- **Interaction plan**: at least type/scenario switching, object inspection,
  and the unified controls.

## 3. Quality bars (what disqualifies a benchmark)

- Same boxes-and-arrows for all knowledge points → fail (Q1).
- Four transfer types drawn with identical rhythm → fail (the mechanism IS
  the timing).
- Fields with fixed decorative numbers where live computation is possible →
  fail (same-data rule).
- Any unsourced `SPEC` claim, or an invented clause number → fail (accuracy
  gate).

## 4. Deliverables per benchmark

1. `design.md` — the three art directions + selection + motion storyboard.
2. `index.html` — the runnable animation (self-contained, no build step).
3. Screenshots — initial / mid / end / exception / narrow-720 (from the
   real-browser suite).
4. Test report — technical gate output (validators + browser suite) and
   functional assertions.
5. Scoring sheet — the six-dimension visual-scoring.md rubric, filled with
   the reviewer's actual numbers and evidence pointers.
6. Known limitations — honest list.

## 5. Result recording

Store under `benchmarks/results/<benchmark-name>.md` with:
score table (per dimension + weighted total), evidence links (screenshot
paths, test output), reviewer identity, date, and any N/A dimensions with
re-weighting shown. Never fill scores aspirationally — a missing measurement
stays `UNMEASURED`.

## 6. Current benchmark set

| Benchmark | Topic | Level | Notes |
|---|---|---|---|
| usb-enumeration | insertion → reset → control-transaction enumeration → Configured | L3 | state tower + camera; descriptor inspection |
| usb-packet-structure | waveform→packet→exploded field anatomy | L3 | live spec-exact CRC5/CRC16 (§8.3.5), binary/hex, editable fields |
| usb-transfer-types | control / bulk / interrupt / isochronous scheduling rhythms | L3 | frame-timeline instrument; per-type mechanics incl. no-handshake iso |
