# Interaction Design for Teaching Animations

Interaction turns a movie into an experiment. But every interactive element
must serve the learning objective; interactions that only decorate add
cognitive load (see animation-taxonomy.md §coherence).

## 1. Defaults first

The page must teach on first load **without any interaction**: correct
initial state, visible caption, obvious controls. Interaction deepens; it
never gates basic understanding.

## 2. Playback controls

- Follow the unified contract (timeline-control.md): play/pause, step,
  reset required; speed and timeline scrub recommended.
- Buttons ≥ 32 px hit area, `aria-label`s, visible focus.
- Step buttons are the most under-used teaching tool: they let the learner
  ask "what exactly changed here?" — place them prominently, and make each
  step a *cause→effect* unit.

## 3. Parameters (for simulations)

- One row per parameter: label, current value, input control, unit.
- Ranges: physically meaningful, clamped; `step` sized so small changes are
  visible. Defaults = the textbook case.
- **Every parameter change must immediately update graphics AND every
  dependent number.** A slider that moves a waveform but not the RMS readout
  is a bug (the same-data rule).
- Show the *formula with live numbers* at least once on the page
  (e.g. `V_avg = D × V_supply = 0.40 × 5.0 V = 2.0 V`).
- Prefer 2–5 parameters. Need more? Group under an "Advanced" disclosure.
- Changing parameters while paused re-renders at current `t` — the learner
  can freeze a moment and experiment on it.

## 4. Scenarios

Named presets that configure parameters + start conditions:

- `default` — the canonical story.
- at least one **exception scenario** (timeout, NAK/retry, WC mismatch,
  overload) — exception paths are where real understanding lives.
- optionally edge cases (min/max values).

Scenario switch = set params + `seek(0)`. The selected scenario is visible
in the UI at all times.

## 5. Explanations and captions

- Caption text always matches the current step (same data source, never a
  parallel timer).
- Keep a "What changed?" quality: state the cause and the effect, name the
  object by its on-screen label.
- Optional per-step "detail" notes may live under the caption (details
  element) for depth without clutter.

## 6. Anti-patterns

- Autoplaying sound; blinking/bouncing decoration; parallax.
- Hidden interactions (no affordance) — if it's clickable it must look and
  read as clickable.
- Interactions that fight the timeline (a "shuffle" button that mutates
  state outside `render`).
- Ten simultaneous sliders "because users might want them".
- Tooltips as the only place a key number appears.
