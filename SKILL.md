---
name: technical-animation-engineer
description: Create, analyze, optimize, and audit interactive HTML/SVG/JavaScript animations that teach engineering and technology topics (network protocols such as Ethernet, EtherCAT, USB, BLE, Wi-Fi; embedded systems such as FOC, motor control, FreeRTOS, DMA, ADC, PWM, SPI, I2C, UART; plus OS, computer architecture, digital/power electronics, math and physics). Use this skill when the user asks to build a technical teaching animation, convert a protocol/hardware/algorithm concept into an interactive visualization, turn a static diagram into an animation, or review, fix, or refactor an existing HTML tutorial's animations. Enforces technical-accuracy-first storyboarding with evidence tagging (SPEC/VENDOR/CHIP/SDK/TEACHING), a unified play/pause/step/reset/speed/timeline control contract, five animation type templates, visual and accessibility design rules, and automated HTML validation scripts.
license: "MIT (code) / CC-BY-4.0 (docs); see LICENSE and LICENSE-DOCS in the repository root"
compatibility: "Output is self-contained HTML/CSS/JS with no build step. Skill scripts require Python 3.8+. Optional: Node.js for JS syntax checks, Playwright for browser tests."
metadata:
  version: "1.0.0"
  maintained_by: "Technical Animation Engineer contributors"
---

# Technical Animation Engineer

Turn engineering knowledge — protocols, electronics, motor control, RTOS
behavior, computer architecture, physics — into **technically correct,
interactive HTML/SVG/JavaScript teaching animations**.

**Core principle: Technical Accuracy First. Visual Quality Second.**
Every visual decision serves the knowledge being taught. Anything shown on
screen must be technically defensible. An animation that looks good and
teaches something wrong is a failure.

## Workflow (follow this order; gates are mandatory)

1. **Analyze** — understand the knowledge point; if working on an existing
   page, complete the audit first (see "Auditing an existing tutorial").
2. **Design** — technical analysis → animation mapping → storyboard
   ([assets/storyboard-template.md](assets/storyboard-template.md)).
3. **Validate the design** — every claim classified and sourced in the
   Evidence Table ([references/technical-accuracy.md](references/technical-accuracy.md)).
   **Gate: a storyboard with unconfirmed technical basis must not enter
   implementation.**
4. **Implement** — page spec
   ([assets/animation-spec-template.md](assets/animation-spec-template.md)),
   then code ([references/svg-animation.md](references/svg-animation.md),
   [references/timeline-control.md](references/timeline-control.md),
   [references/visual-design.md](references/visual-design.md)).
5. **QA** — run the validation scripts, test in a real browser, do a
   screenshot review
   ([references/animation-testing.md](references/animation-testing.md),
   [references/visual-review.md](references/visual-review.md)), record
   results in
   [assets/validation-report-template.md](assets/validation-report-template.md).

## Evidence tags (mandatory for every animation)

| Tag | Meaning | Rule |
|---|---|---|
| `SPEC` | Defined by a public standard (USB 2.0 ch.9, ETG.1000, Bluetooth Core) | Cite standard + clause in the storyboard |
| `VENDOR` | One vendor's implementation (STM32 HAL, TI's Clarke convention) | Never present as the generic standard |
| `CHIP` | Silicon-specific limit or behavior (datasheet, errata) | Name the chip |
| `SDK` | Software stack behavior (FreeRTOS kernel, HAL library) | Name the stack + version |
| `TEACHING` | Deliberate simplification | **Must be labeled on the page itself** |
| `VERIFIED` | Confirmed against a citable source | Record the source |
| `UNVERIFIED` | Not confirmed | **Release blocker — source it or drop it** |

Hard rules:
- Protocol message order and timing must not be altered for visual effect.
- Never present vendor or SDK behavior as "how it works" in general.
- Never present a teaching simplification as real hardware behavior.
- If you cannot confirm a behavior, stop that part of the animation and tell
  the user. Do not guess silently.

## Five animation types

| Type | Use for | Reference |
|---|---|---|
| A. Protocol Sequence | USB enumeration, EtherCAT exchange, BLE advertising/connection, Wi-Fi association | [references/animation-taxonomy.md](references/animation-taxonomy.md) |
| B. Data Flow | Ethernet/USB packets, DMA transfers, memory copy, SPI/I2C exchange | same |
| C. State Machine | Device/task/driver states, boot processes | same |
| D. Physical Mechanism | FOC transforms, PWM, ADC sampling, magnetic fields | same |
| E. Interactive Simulation | anything where changing a parameter must change the computed result | same |

Not every concept needs an animation. If a static diagram explains it better,
use a static diagram (decision rules in the taxonomy reference).

## Unified control contract

Interactive animations expose consistent controls via data attributes:

| Attribute | Element | Behavior |
|---|---|---|
| `data-tae-action="play-pause"` | button | toggle; resume must be exact |
| `data-tae-action="step-fwd"` / `"step-back"` | button | exactly one defined step |
| `data-tae-action="reset"` | button | restores ALL state, incl. user parameters |
| `data-tae-action="speed"` | select | multiplies story-time rate |
| `data-tae-action="scenario"` | select | named presets (incl. an exception scenario) |
| `data-tae-timeline` | input range | scrub maps to story time |
| `data-tae-caption` | caption container | text always matches current step |

Architecture rules (full spec in
[references/timeline-control.md](references/timeline-control.md)):
- One timing source per page: a single timestamp-driven
  `requestAnimationFrame` loop. **Never** combine `setInterval` timers.
- `render(t, params)` is a pure function of timeline position + parameters;
  all graphics and all displayed numbers derive from it.
- Expose `window.__TAE__` (state + seek/step/reset API) so tests can drive
  the animation.

## Implementation stack

Default: hand-written HTML5 + CSS3 + vanilla JS + SVG, single self-contained
file, no build step. Use the Web Animations API or Canvas only where SVG/CSS
is insufficient. Add a library (D3, GSAP, Three.js) only when the knowledge
genuinely requires it and the license is recorded — never to make a simple
concept look impressive. Techniques: [references/svg-animation.md](references/svg-animation.md).

## Testing (run, don't assume)

```bash
# from the repository root (skill installed at .agents/skills/technical-animation-engineer)
SKILL=.agents/skills/technical-animation-engineer
python $SKILL/scripts/validate_skill.py $SKILL          # skill structure
python $SKILL/scripts/validate_html.py <page.html>       # static HTML checks
python $SKILL/scripts/validate_animation.py <page.html>  # control contract
node tests/browser-tests/run_browser_tests.mjs           # Playwright browser suite (optional)
```

- `validate_html.py` / `validate_animation.py` exit 1 on errors. Fix errors;
  judge remaining warnings (they are recommendations).
- Static checks are not acceptance. A passing page still needs real-browser
  interaction tests and a screenshot review
  ([references/animation-testing.md](references/animation-testing.md),
  [references/visual-review.md](references/visual-review.md)).
- Record what was actually tested. Never report untested checks as passed.

## Auditing an existing tutorial

When asked to analyze/optimize/refactor an existing HTML tutorial:

1. Read the page(s); inventory every animation module (DOM/JS/SVG entry points).
2. For each: knowledge point, animation type, implementation method,
   interaction set.
3. Check text ↔ animation consistency and technical accuracy per module.
4. Produce a written audit report **before changing anything**. No mass edits
   before the audit exists and the user has seen it.
5. Fix or rebuild per module, starting with technically wrong content.

## Reference loading map

| When you need to… | Read |
|---|---|
| Choose an animation type; decide animate vs static diagram | [references/animation-taxonomy.md](references/animation-taxonomy.md) |
| Classify/verify claims; handle uncertainty | [references/technical-accuracy.md](references/technical-accuracy.md) |
| Write a storyboard; audit an existing tutorial | [references/storyboard-method.md](references/storyboard-method.md) |
| Implement SVG/JS animation techniques | [references/svg-animation.md](references/svg-animation.md) |
| Build the play/pause/step/reset/timeline system | [references/timeline-control.md](references/timeline-control.md) |
| Style the page (color semantics, typography, themes) | [references/visual-design.md](references/visual-design.md) |
| Design interactions and parameter panels | [references/interaction-design.md](references/interaction-design.md) |
| Make it accessible (reduced motion, contrast, keyboard) | [references/accessibility.md](references/accessibility.md) |
| Plan and run QA | [references/animation-testing.md](references/animation-testing.md) |
| Do the screenshot-based visual review | [references/visual-review.md](references/visual-review.md) |

## Common pitfalls (do not do these)

- Building the animation before the storyboard is technically validated.
- One "timer" per visual effect instead of one timeline — state desyncs on
  pause/scrub.
- Fake numbers: an arrow "rotates" while the equation panel shows values not
  computed from the same data.
- Only the happy path: no timeout/retry/exception scenario.
- Decorative motion (pulsing, bouncing) that adds no information.
- Presenting a specific chip's behavior as the general standard.
- Labelling page files with invented sources. If no source, tag `UNVERIFIED`.

## License note

Code in `scripts/` is MIT-licensed; this documentation is CC-BY-4.0. See
`LICENSE` and `LICENSE-DOCS` in the repository root. Animations you author
with this skill are yours; if you publish them, keep the evidence tags — they
are what makes the page trustworthy.
