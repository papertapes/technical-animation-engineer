# Animation Testing

Testing pyramid, cheapest first. A level may only be skipped for
**deliberately omitted** controls (record it in the animation spec).

```
static checks → contract checks → runtime (real browser) → state tests → visual review → VISUAL QUALITY GATE
```

Two gates close the pyramid. The **technical gate** (levels 1–5 plus the
defect-focused visual review) proves the page is correct and robust. The
**visual quality gate** ([visual-quality-gate.md](visual-quality-gate.md))
proves it is worth watching — scored 10-question review with old-vs-new
comparison. Both must pass for L2–L3 pages; a page that is only correct, or
only pretty, fails.

Determinism rule for motion design: **camera, scenes, particles and effects
are part of `render(t, params)`** — asserted by scrubbing: scrub to any t,
capture, scrub away and back to the same t, capture again; the frames must
match. CSS/JS keyframe freewheeling for story motion fails this test and the
contract.

## 1. Static checks — `validate_html.py`

```bash
python scripts/validate_html.py page.html        # or a directory
```

Checks: tag well-formedness (strict), duplicate ids, missing local
resources, dangling in-page anchors, `<title>`/`lang`/viewport, `<img>`
alt, `<style>` brace balance, inline-JS syntax via `node --check` (skipped
gracefully without Node), forbidden APIs (`document.write`, `eval`), and an
inventory of external references (feeds the license review). Exit 1 on
errors.

## 2. Contract checks — `validate_animation.py`

```bash
python scripts/validate_animation.py page.html
```

Checks the unified control contract: required play/pause + reset, recommended
step/speed/timeline/caption/evidence tags/`window.__TAE__`/reduced-motion,
anti-patterns (multiple `setInterval`, inline `onclick`, `alert`, duplicate
step ids), plus everything from level 1. Exit 1 on errors.

## 3. Runtime checks — real browser

Either run the bundled Playwright suite:

```bash
cd tests/browser-tests
npm install && npx playwright install chromium   # once
node run_browser_tests.mjs                        # all pages
```

The suite per page: zero console/page errors; play → mid screenshot → pause
→ step → reset → speed change → scrub; saves screenshots; exits non-zero on
any console error or failed control interaction.

Or drive ZCode/agent browser automation the same way. **A page that was
never opened in a browser is untested**, whatever the static checks say.

## 4. State tests (state machines & protocols)

Drive `window.__TAE__` (or the UI) to assert behavior:

- initial state correct at `t=0`
- **every legal transition** visited (enumerate them from the storyboard)
- illegal transition attempts don't corrupt state (e.g. IN before SETUP
  never occurs even when scrubbing wildly)
- exception branch reachable (run its scenario)
- final state correct; after `reset()` state equals initial state

```js
// example assertions
TAE.seek(0); assert(state === "default");
for (const step of TAE.steps) { TAE.seek(step.start); assert(expectedState(step.id) === state); }
TAE.reset(); assert(deepEqual(state, initialState));
```

## 5. Simulation-consistency tests (interactive sims)

- Set parameter to min / max / mid: graphics **and** every displayed number
  recomputed and mutually consistent (e.g. displayed D matches slider,
  `V_avg = D·V_supply` arithmetic holds, waveform period matches 1/f).
- Pause → change parameter → frame updates coherently; resume unaffected.

## 6. Visual review

Separate discipline — screenshots, not code:
[visual-review.md](visual-review.md). Never claim visual acceptance from
code checks alone.

## 7. Recording results honestly

- Paste actual tool output into the validation report
  ([assets/validation-report-template.md](../assets/validation-report-template.md)).
- Untested ≠ passed. Mark untested checks as **UNTESTED** with the reason.
- Every fix is re-verified by re-running the failing check (and its
  neighbors), not by assumption.
