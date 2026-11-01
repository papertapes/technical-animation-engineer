---
name: technical-animation-engineer
description: "Create, upgrade, and audit interactive HTML/SVG/Canvas/JS animations that teach engineering topics (protocols: Ethernet, EtherCAT, USB, BLE, Wi-Fi; embedded systems: FOC, motor control, FreeRTOS, DMA, PWM, UART; plus OS, architecture, electronics, math and physics) with professional motion design: visual storytelling, motion graphics, cinematic camera work, and interactive simulation. Use this skill when the user asks to build a technical teaching animation, visually upgrade or redesign an existing tutorial animation, turn a protocol/hardware/algorithm concept into an interactive visualization, or review/fix/refactor an existing HTML tutorial's animations. Enforces technical accuracy with evidence tags (SPEC/VENDOR/CHIP/SDK/TEACHING), visual concept and motion storyboards before code, three visual quality levels (default professional-to-cinematic), a unified play/pause/step/reset/speed/timeline control contract, an independent visual quality gate, and automated HTML validation."
license: "MIT (code) / CC-BY-4.0 (docs); see LICENSE and LICENSE-DOCS in the repository root"
compatibility: "Output is self-contained HTML/CSS/JS with no build step. Skill scripts require Python 3.8+. Optional: Node.js for JS syntax checks, Playwright for browser tests."
metadata:
  version: "2.1.0"
  maintained_by: "Technical Animation & Motion Design Engineer contributors"
---

# Technical Animation & Motion Design Director

Turn engineering knowledge — protocols, electronics, motor control, RTOS
behavior, computer architecture, physics — into **technically correct,
visually striking, interactive HTML/SVG/Canvas/JavaScript teaching
animations**.

**Core principles:**
1. **Technical Accuracy First.** Anything shown must be technically
   defensible. A beautiful page that teaches something wrong is a failure.
2. **Visual Quality Second — and mandatory.** A technically correct page that
   is still "boxes and arrows" is *also* a failure. Flatness is a defect.
3. **Storytelling is the delivery vehicle.** Effects must encode the knowledge
   (particle speed = scaled signal rate; zoom = where the answer lives);
   decoration that carries no information is removed.

## Visual quality levels

Every animation declares a target level (recorded in its visual concept):

| Level | Name | Typical traits |
|---|---|---|
| L1 | Basic technical visualization | clean schematic motion, simple transitions — acceptable only for minor supporting content |
| L2 | Professional motion graphics (**default floor**) | dynamic data streams, layered depth, glow/emphasis, precise timing, dynamic typography, meaningful highlights |
| L3 | Cinematic interactive experience | camera moves (zoom/pan/focus), scene transitions, particle/light effects, exploded views, interactive exploration |

Default target is **L2–L3**. Drop to L1 only with a stated reason (minor
point, tiny widget). Never sacrifice comprehension for spectacle.

## Workflow (ten steps; gates are mandatory)

**Step 1 — Technical Understanding.** Objects, mechanism, data structures,
states, timing, key events, exception paths, standard basis, vendor
differences ([references/technical-accuracy.md](references/technical-accuracy.md)).

**Step 2 — Visual Storytelling.** Before any code: the hero moment, what gets
zoomed/cutaway, what the learner sees first
([references/visual-storytelling.md](references/visual-storytelling.md),
[assets/visual-concept-template.md](assets/visual-concept-template.md)).

**Step 3 — Art Direction.** Propose **2–3 clearly different visual
directions** (archetypes: Cinematic Dark Laboratory, Scientific Instrument,
Technical Editorial, Blueprint, Kinetic Infographic — see
[references/art-direction.md](references/art-direction.md)); compare, select
the strongest teaching fit, record why.

**Step 4 — Storyboard.** Scene sheet: Scene ID, purpose, knowledge point,
objects, composition ([references/composition-and-layout.md](references/composition-and-layout.md)),
camera, motion ([references/motion-language.md](references/motion-language.md)),
time range, interactions, end state
([assets/motion-storyboard-template.md](assets/motion-storyboard-template.md)).

**Step 5 — High-Fidelity Prototype.** A runnable independent HTML with full
visual design and real motion — never a static mock, and never a direct edit
of an existing tutorial page at this stage.

**Step 6 — Visual Review.** Focal point present? hierarchy clear? rhythm
natural? transitions smooth? objects refined? boxes-and-arrows escaped? no
meaningless decoration?
([references/visual-hierarchy.md](references/visual-hierarchy.md)).

**Step 7 — Technical Validation.** The visual may not change real behavior;
states are driven by the simulation, numbers by the same data
([references/technical-accuracy.md](references/technical-accuracy.md)).

**Step 8 — Integration.** Merge into the host tutorial only after acceptance;
preserve its content, navigation, progress and other widgets.

**Step 9 — Regression Testing.** Host tutorial unaffected + new animation
passes the technical gate
([references/animation-testing.md](references/animation-testing.md)).

**Step 10 — Final Review.** Old-vs-new comparison screenshots, real browser
run, visual scoring ([references/visual-quality-gate.md](references/visual-quality-gate.md),
[references/benchmark-design.md](references/benchmark-design.md)). No claim of
visual acceptance without a real browser run.

## Evidence tags (mandatory for every animation)

| Tag | Meaning | Rule |
|---|---|---|
| `SPEC` | Defined by a public standard | cite standard + part/clause in the storyboard |
| `VENDOR` | One vendor's implementation | never present as the generic standard |
| `CHIP` | Silicon-specific behavior/limit | name the chip |
| `SDK` | Software stack behavior | name the stack + version |
| `TEACHING` | Deliberate simplification | **must be labeled on the page itself** |
| `VERIFIED` / `UNVERIFIED` | claim status | UNVERIFIED is a release blocker |

Hard rules: protocol order/timing never altered for effect; vendor ≠
standard; simplification ≠ reality; same data drives pixels and numbers; if
unconfirmable — stop that part and say so.

## Five animation types

| Type | Use for | Reference |
|---|---|---|
| A. Protocol Sequence | enumeration, frame exchange, association | [references/animation-taxonomy.md](references/animation-taxonomy.md) |
| B. Data Flow | packets, DMA, buffers, pipelines | same |
| C. State Machine | device/task/driver states | same |
| D. Physical Mechanism | FOC, PWM, ADC, fields | same |
| E. Interactive Simulation | parameter sensitivity | same |

Not every concept needs an animation — decision rules in the taxonomy.

## Unified control contract

| Attribute | Element | Behavior |
|---|---|---|
| `data-tae-action="play-pause"` | button | toggle; resume exact |
| `data-tae-action="step-fwd"` / `"step-back"` | button | exactly one defined step |
| `data-tae-action="reset"` | button | restores ALL state incl. parameters |
| `data-tae-action="speed"` | select | story-time multiplier |
| `data-tae-action="scenario"` | select | presets incl. exception scenario |
| `data-tae-timeline` | range | scrub = story time |
| `data-tae-caption` | container | text always matches current step |

Architecture rules
([references/timeline-control.md](references/timeline-control.md)):
one timestamp-driven `requestAnimationFrame` loop; `render(t, params)` pure —
**camera (viewBox), scene visibility, particles, glow, and every displayed
number derive from `(t, params)`**; expose `window.__TAE__` for tests. Cinematic
techniques never excuse a second timer.

## Motion & cinematic stack

- **Default:** hand-written HTML5 + CSS + vanilla JS + **SVG** (and **Canvas**
  for particle-heavy scenes), single self-contained file, no build step.
  Web Animations API allowed for one-shot effects (story clock stays the rAF loop).
- **Three.js**: only for genuinely 3D structure (package internals, 3D fields);
  MIT; heavier page — document the choice.
- **GSAP / D3 / Motion**: allowed for non-redistributed projects when the
  effect genuinely requires it. License check first — **GSAP is not open
  source** (custom "no charge" license; never bundle it into redistributable
  open-source teaching files). Record any dependency in THIRD_PARTY_NOTICES.
- Effects catalog + implementation recipes:
  [references/motion-graphics.md](references/motion-graphics.md). Camera work,
  transitions, depth, lighting: [references/cinematic-animation.md](references/cinematic-animation.md).
- Visual tokens & stage themes (incl. cinematic dark stage):
  [references/visual-design.md](references/visual-design.md).

## Visual Quality Gate (independent of the technical gate)

Ten questions — "is it still boxes and arrows?", "is there a hero moment?",
"is attention guided?", … — plus a hard rule: **background colors, fonts,
rounded corners, shadows, plain gradients, box sizes and arrow colors alone
do not constitute an upgrade.** Score against the old version; if not clearly
better, iterate. Full rubric:
[references/visual-quality-gate.md](references/visual-quality-gate.md).

## Testing (run, don't assume)

```bash
SKILL=.agents/skills/technical-animation-engineer
python $SKILL/scripts/validate_skill.py $SKILL          # skill structure
python $SKILL/scripts/validate_html.py <page.html>       # static HTML checks
python $SKILL/scripts/validate_animation.py <page.html>  # control contract
node tests/browser-tests/run_browser_tests.mjs           # Playwright browser suite (optional)
```

Static checks are not acceptance: every page needs real-browser interaction
tests **and** both review gates. Record what was actually tested; untested
checks stay marked UNTESTED.

## Auditing an existing tutorial

1. Inventory every animation module (DOM/JS/SVG entry points, libraries).
2. Per module: knowledge point, type, **current visual level (L1/L2/L3)**,
   implementation, interactions, text↔animation consistency, technical
   accuracy.
3. Written audit report **before any change** — no mass edits before the
   user has seen it. Severity: Blocker (teaches something wrong) / Major
   (broken state management, dead controls) / Minor / Polish.
4. Fix or rebuild per module; each upgrade must pass **both** gates before
   moving on. Preserve the host tutorial's content, structure, navigation and
   progress management unless the user asks otherwise.

## Reference loading map

| When you need to… | Read |
|---|---|
| Choose type / level; decide animate vs static | [references/animation-taxonomy.md](references/animation-taxonomy.md) |
| Run the art-direction generator (2–3 directions) | [references/art-direction.md](references/art-direction.md) |
| Choose composition per scene | [references/composition-and-layout.md](references/composition-and-layout.md) |
| Apply the motion language (six questions per motion) | [references/motion-language.md](references/motion-language.md) |
| Enforce information hierarchy | [references/visual-hierarchy.md](references/visual-hierarchy.md) |
| Study external references legally | [references/visual-reference-analysis.md](references/visual-reference-analysis.md) |
| Design/verify benchmarks | [references/benchmark-design.md](references/benchmark-design.md) |
| Write the fact storyboard; audit method details, severity levels | [references/storyboard-method.md](references/storyboard-method.md) |
| Design the story: hero moment, scenes, attention flow | [references/visual-storytelling.md](references/visual-storytelling.md) |
| Pick & implement effects (particles, glow, morph, exploded view…) | [references/motion-graphics.md](references/motion-graphics.md) |
| Camera moves, transitions, depth, lighting | [references/cinematic-animation.md](references/cinematic-animation.md) |
| Classify/verify claims; handle uncertainty | [references/technical-accuracy.md](references/technical-accuracy.md) |
| Implement SVG/JS/Canvas techniques | [references/svg-animation.md](references/svg-animation.md) |
| Build the play/pause/step/reset/timeline system | [references/timeline-control.md](references/timeline-control.md) |
| Style the page (tokens, stage themes, typography) | [references/visual-design.md](references/visual-design.md) |
| Design interactions and parameter panels | [references/interaction-design.md](references/interaction-design.md) |
| Make it accessible (reduced motion, contrast, keyboard) | [references/accessibility.md](references/accessibility.md) |
| Plan and run QA (technical gate) | [references/animation-testing.md](references/animation-testing.md) |
| Defect review (overflow/overlap/contrast) | [references/visual-review.md](references/visual-review.md) |
| Score expressiveness; old-vs-new comparison | [references/visual-quality-gate.md](references/visual-quality-gate.md) |

## Common pitfalls (do not do these)

- Coding before the visual concept exists; skipping the storyboard.
- **Restyle-only "upgrades"** (colors, fonts, shadows, gradients) — explicitly
  rejected by the visual quality gate.
- Decoration that carries no information; effects contradicting the data.
- One timer per effect; camera/effects outside `render(t, params)`.
- Fake numbers; only the happy path; unlabeled simplifications.
- Presenting vendor behavior as the standard; invented sources.
- Text rotated/blurred by camera moves; unreadable glow-on-glow contrast.

## License note

Code in `scripts/` is MIT; documentation is CC-BY-4.0 (`LICENSE`,
`LICENSE-DOCS` in the repository root). Animations you author are yours —
keep the evidence tags and pass both gates before publishing.
