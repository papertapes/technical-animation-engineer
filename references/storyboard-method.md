# Storyboard Method & Tutorial Audit

No important animation starts as code. The pipeline is:
**Technical Analysis → Animation Mapping → Storyboard → Technical Validation
→ Implementation → QA.** Gates between stages are mandatory.

## 1. Technical Analysis (before any design decision)

Answer these ten questions in writing; unclear answers block design:

1. What problem does this knowledge point solve?
2. What is the actual working mechanism (per sources, not per intuition)?
3. Which devices/actors are involved?
4. Which data is involved (fields, sizes, values)?
5. Which states exist?
6. Which timing/ordering relationships exist?
7. Which parts are standard-defined (`SPEC`)?
8. Which parts are vendor/chip/SDK-specific (`VENDOR`/`CHIP`/`SDK`)?
9. Which parts will we simplify (`TEACHING`) — and how, exactly?
10. What is still unconfirmed (`UNVERIFIED`) — and can we proceed?

## 2. Animation Mapping

Map: **knowledge point → learning objective → animation type → animation
objects → interaction.**

- The learning objective is a learner capability ("can predict what happens
  on timeout"), never "understands X".
- Choose the type with
  [animation-taxonomy.md](animation-taxonomy.md). One animation = one
  primary type; secondary patterns (e.g. a state strip inside a sequence
  animation) are fine.
- **Static beats animated** when the content is a structure (a memory map),
  a taxonomy, or anything with no meaningful time dimension. Animation pays
  off when *order*, *causality*, *change over time*, or *parameter
  sensitivity* is the point.

## 3. Storyboard

Fill [assets/storyboard-template.md](../assets/storyboard-template.md)
completely. Quality bars:

- **Step granularity:** one step = one observable cause→effect ("UART TXE
  fires → DMA writes next byte"). If a step needs "and then … and then …",
  split it.
- **Steps carry state changes**, not just visuals: what value changed, where.
- **Exception steps exist:** at least one timeout/retry/error path, or an
  explicit scenario for it.
- **Captions are assertions**, not narration: "The working counter is now 2 —
  Slave 2 processed the datagram" beats "Now we see the frame moving on".
  Maximum two sentences per caption.
- **Timing is explicit:** real value (e.g. "≥ 10 ms reset"), story-time
  duration, and the scaling factor between them.

## 4. Technical Validation (gate)

Before implementation, review the storyboard against
[technical-accuracy.md](technical-accuracy.md):

- [ ] Every Evidence Table row has a tag and a source (or is honest `TEACHING`)
- [ ] No `UNVERIFIED` claims remain
- [ ] Message/order/timing matches the source material
- [ ] Exception branches are real behaviors, not invented drama
- [ ] The learning objective is actually served by the chosen scenes
- [ ] A domain-knowledgeable reviewer (human, or a separate agent pass)
      has checked the storyboard

If validation fails → fix the storyboard, not the standard.

## 5. Implementation

Fill [assets/animation-spec-template.md](../assets/animation-spec-template.md)
(scene layout, object inventory, state model, control matrix) **before**
coding. Implement per [svg-animation.md](svg-animation.md) and
[timeline-control.md](timeline-control.md).

## 6. QA

Run [animation-testing.md](animation-testing.md) checks and the screenshot
review [visual-review.md](visual-review.md); record results in
[assets/validation-report-template.md](../assets/validation-report-template.md).

## 7. Auditing an existing tutorial

When the task is to analyze/optimize/refactor an existing page, the audit
comes first — **no mass edits before the audit exists.**

### Audit procedure

1. Load the page in a browser; open devtools; note console errors up front.
2. Inventory the code: entry HTML, CSS organization, JS modules, animation
   mechanisms found (rAF loops, intervals, CSS transitions, WAAPI, libraries).
3. Build a module table:

   | Module (selector/function) | Knowledge point | Animation type | Implementation | Interactions | Text↔animation consistent? | Technically correct? |
   |---|---|---|---|---|---|---|

4. Check each module for: (a) technical accuracy against sources
   ([technical-accuracy.md](technical-accuracy.md)), (b) text/animation
   consistency, (c) state-management sanity (timers, reset, scrubbing),
   (d) interaction completeness, (e) visual issues (overflow, overlap,
   contrast) via screenshots.
5. Write the audit report: findings per module, severity
   (blocker / major / minor / polish), and a recommended action per module
   (fix in place / rebuild / keep).
6. Only after the user has seen the audit: fix or rebuild module by module,
   re-running QA per module.

### Audit severity levels

- **Blocker** — teaches something wrong (wrong order, wrong physics,
  wrong model); fix before anything cosmetic.
- **Major** — broken state management, dead controls, desynced captions.
- **Minor** — visual issues, missing steps/speed controls.
- **Polish** — styling, wording, accessibility improvements.
