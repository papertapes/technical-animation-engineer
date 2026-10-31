# SVG & JS Animation Techniques

Default stack: **hand-written HTML5 + CSS3 + vanilla JS + SVG in a single
self-contained file** (opens from `file://`, no build step, no network).
Reach for more only when justified (see §7).

## 1. Choosing the rendering technique

| Need | Technique |
|---|---|
| 2D technical diagrams, signals, data flow | SVG (default) |
| Simple state changes (highlight, color, visibility) | CSS transitions/classes |
| Simulation loop (positions from `t`) | one rAF loop updating SVG attrs/styles |
| One-shot choreographed transitions | Web Animations API (`element.animate`) |
| Hundreds of dynamically moving objects | Canvas 2D |
| True 3D structure (chip packages, motor geometry) | Three.js (rarely justified) |
| Data-driven charts/axes | small hand-rolled SVG axes or D3 scales |

## 2. SVG structure that stays maintainable

- Set `viewBox`; scale responsively with `width: 100%; height: auto`.
- One `<g>` per **semantic object** (`id="device-host"`, `id="pkt-1"`), not
  per visual effect. State changes select objects, never pixels.
- Reuse shapes with `<defs>` + `<use>` (devices, packets, arrowheads).
- Arrows: `marker` elements; direction lives in the geometry — verify
  visually that marker orientation is correct (auto-start-reverse).
- Text in SVG: keep it horizontal, anchor deliberately (`text-anchor`),
  never scale text non-uniformly; prefer HTML overlays for paragraphs.
- Label layers with comments; order = paint order (later paints on top).

## 3. Efficient per-frame updates

Inside the rAF loop:

- Cache element references at init (`const el = id => document.getElementById(id)`).
- Prefer `transform` (translate/rotate) and `opacity` — cheap to composite.
  For SVG group moves: `g.setAttribute('transform', 'translate(x,y)')` or
  `g.style.transform` (CSS transforms on SVG work in all modern browsers;
  pick one style per file and stay consistent).
- Batch writes; never read layout (`getBoundingClientRect`) and write in the
  same frame repeatedly (layout thrashing).
- Avoid per-frame allocations (no `new` objects/arrays/closures in the loop).
- Don't create/destroy nodes per frame; toggle visibility / move existing ones.
- Number displays: update only when the value actually changes (string
  compare) to avoid text layout work every frame.

## 4. Attribute vs CSS vs WAAPI

- **Attribute/style updates from `render(t, params)`** — the default for
  anything timeline-driven (positions, counters, buffer cells, progress).
- **CSS transitions** — for instantaneous state changes that should ease
  (class swap: `.active`, `.error`), kept short (≤300 ms) so they don't
  fight the timeline.
- **Web Animations API** (`el.animate(...)`) — for self-contained one-shot
  effects (a pulse when a packet is emitted). Play/pause of the *story* must
  never depend on WAAPI clock; the story clock is the rAF loop.

## 5. JavaScript hygiene

- Strict mode; no globals except the documented `window.__TAE__`.
- Constants for geometry/timings at the top (`const STEP_MS = 1200`).
- Event listeners added once at init (never inside `render`); use
  delegation on the controls container.
- No `eval`, no `document.write`, no `alert`; `console.log` only for
  debugging, removed before delivery.
- Everything derived from `(t, params)` — resist "just set a flag here".
- Keep JS in one `<script>` block with clear sections:
  constants → state → render → controls → init.

## 6. Responsiveness

- SVG scales via `viewBox`; keep minimum text legible at 360 px wide
  (short labels, `font-size ≥ 11px` equivalent).
- Controls wrap (`flex-wrap: wrap`); parameter panel stacks below the stage
  on narrow screens.
- Test at 1280 px and 720 px widths (see animation-testing.md).

## 7. When a library is justified

Add a dependency only when ALL hold: the knowledge genuinely needs it
(true 3D, complex chart axes), the page cannot reasonably implement it in
≤100 lines, the license is compatible and recorded in
`THIRD_PARTY_NOTICES.md`, and the delivery mode accepts it (inline a vendored
copy or require network — document which). Otherwise ship vanilla.
A 60-line hand-rolled timeline beats 300 kB of "convenience".
