# Motion Graphics Catalog & Recipes

A catalog of professional effects **and the rules for earning them**. Choose
effects per knowledge point — an effect must encode data or direct attention;
stacking effects without meaning fails the visual quality gate.

Universal rules:
- Every effect is computed inside `render(t, params)` (deterministic — pause,
  scrub and step reproduce it exactly).
- Performance budget: no node creation per frame; ≤ ~200 live particles;
  animated filters minimized (animate opacity/transform of pre-glowed layers
  instead of re-blurring each frame).
- `prefers-reduced-motion`: ambient/looping effects off; story progresses via
  steps; nothing essential conveyed by motion alone (pair with a lit state or
  caption).

## 1. Particle system — *data rate, activity, "aliveness" of a channel*
- Communicates: throughput, activity, randomness in physical processes.
- Implementation: Canvas overlay (or ≤ 200 SVG circles pooled at init);
  particles emitted at a rate ∝ the *actual scaled rate* (baud, interrupt
  rate); position integrated in the rAF loop from `(t, params)` seeds.
- Discipline: particle speed/density must match the labeled data rate; a
  paused timeline freezes particles (recompute from t, don't free-run).

## 2. Data stream — *bytes/words traveling a path*
- Packet pill + fading trail (3–5 ghost copies at previous positions);
  stream of small quads for continuous flow; label the payload on the lead unit.

## 3. Signal propagation — *cause traveling down a wire*
- `stroke-dashoffset` animation on the conductor (dash = wavefront), or a
  gradient pulse; propagate at the *scaled* physical speed, and label the
  scaling. For SE0/reset use a two-line drop together.

## 4. Morphing — *same thing changing shape (state/structure change)*
- Interpolate path `d` only between same-structure paths (same command count);
  or crossfade two states + scale. Use for state badges and connector
  re-routing, never for text.

## 5. Dynamic highlight — *this is the explained element*
- Glow: pre-rendered blurred duplicate layer under the shape, opacity keyed
  to focus; outline pulse via `stroke-width`/dash march. Exactly one focal
  glow at a time.

## 6. Waveform animation — *analog truth*
- Scope strip with sweeping cursor (position from t); waveform drawn from the
  same math as the vectors (same-data rule); trigger line, amplitude to scale.

## 7. Layer separation / exploded view — *internal structure*
- Groups translate outward along defined axes, explosion factor = f(t) between
  keyframes; each layer carries its label; leader lines stay attached. The
  signature move for packet/register/stack visuals.

## 8. Path animation — *trajectory with meaning*
- `getPointAtLength` along a defined route (cable, pipeline, ring); constant
  physical velocity stays linear — easing only on starts/stops.

## 9. Glow effect — *energy, live wire, focus*
- SVG filter `feGaussianBlur` on a duplicate, or layered strokes
  (wide+transparent → narrow+solid). Pre-compute once; animate opacity/scale,
  not the filter.

## 10. Light sweep — *activation, "power on", polish*
- Narrow bright gradient band translating across a surface, clipped to the
  shape; use at power-on/enable moments (e.g., VBUS apply, configuration
  accepted). ≤ 700 ms; not an idle loop.

## 11. Dynamic typography — *numbers and titles that participate*
- Counters with tabular numerals; the key value scales up briefly when it
  changes (≤ 250 ms); step titles slide-fade in with the cut. Never bounce body
  text; never animate more than the changed digits.

## 12. Timeline animation — *the story spine*
- The scrub bar is itself a designed object: chapter markers per scene, step
  ticks, progress glow. Learners orient by it.

## 13. Parallax — *depth without 3D*
- Background layer translates at 0.3–0.5× camera rate, mid 1×, foreground
  1.2×; only during camera moves; keep labels on the 1× layer.

## 14. Depth animation — *z as meaning (protocol stacks, encapsulation)*
- Layered planes with slight offset + blur on the farthest (fake DOF); use to
  show encapsulation (frame within frame) or stack traversal (app → TCP → IP
  → MAC).

## 15. Ambient loops — *restrained aliveness*
- Idle breathing (±1.5% scale, 3–4 s), slow dash march on "waiting" wires.
  Disabled under reduced motion; never on text; never competing with the
  focal glow.

## Choosing (anti-stack rule)

For each candidate effect write one line: *"Effect X encodes quantity Y —
remove it and the learner loses Z."* No line, no effect. Multiple effects may
compose when they encode different things (e.g., propagation pulse on the
wire + packet pill carrying the payload + counter ticking on arrival).
