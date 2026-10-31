# Animation Specification: &lt;Animation ID&gt;

> Fill this in after the storyboard passes technical validation and before
> implementation. This is the bridge between storyboard (what to teach) and
> code (how it is built). Companion file: `storyboard.md`.

## 1. Scene Layout

- Canvas: viewBox, coordinate system, responsive behavior (how it reflows at
  narrow widths)
- Regions: stage / caption panel / control bar / parameter panel — which are
  present and where

## 2. Object Inventory

| Object ID | SVG element(s) | Visual token (color / shape semantic) | Interactive? | Layer |
|---|---|---|---|---|
| | | | | |

## 3. State Model

- Story timeline: number of steps, step boundaries in story-time (ms)
- State variables: name, type, legal values, and owner:
  - *timeline-derived* — computed from timeline position, never mutated directly
  - *user parameter* — changed only through inputs, survives seek
- **Rendering rule:** `render(t, params)` must be a pure function of timeline
  position + parameters. All visuals and all displayed numbers derive from it.
  This is what makes pause/resume exact, scrubbing correct, and Reset trivial.

## 4. Control Matrix

| Control | Applies? | Behavior definition |
|---|---|---|
| Play / Pause | | |
| Step Forward | | advances exactly one step boundary |
| Step Backward | | |
| Reset | | restores every variable including user parameters |
| Speed | | multiplier applied to story-time |
| Timeline scrub | | seek to boundary / continuous |
| Scenario switch | | named presets: what each changes |
| Parameter input | | one row per parameter: control, range, effect |

Controls that do not apply to this animation are omitted from the UI on
purpose — record that here so QA does not flag their absence.

## 5. Captions

| Step | Caption text | Sync rule |
|---|---|---|
| | | caption i is visible while t is in step i's interval |

## 6. Implementation Notes

- Timing source: one `requestAnimationFrame` loop; no `setInterval`
- Techniques: SVG attribute updates vs CSS transforms vs Web Animations API —
  which, where, and why
- Accessibility: reduced-motion behavior, aria-labels, keyboard operation
- File layout: single self-contained HTML (preferred for tutorials) or
  shared assets — list them

## 7. Acceptance Checklist (verified during QA)

- [ ] `render(t, params)` is deterministic; scrubbing never corrupts state
- [ ] pause/resume is exact (no drift, no double timers)
- [ ] one step action = exactly one defined step
- [ ] Reset restores all state, including user parameters
- [ ] captions always match the visible step
- [ ] every number shown on screen is computed from the same data that
      drives the graphics (no decorative fake numbers)
- [ ] zero console errors across full interaction script
