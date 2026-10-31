# Cinematic Animation

Camera, scene transitions, depth and lighting for teaching animations — with
the hard constraint: **the camera is part of `render(t, params)`**. Every
move is deterministic, pausable, scrubbable, and must survive the technical
gate (no second timer, no CSS keyframe freewheeling for story motion).

## 1. Camera = animated `viewBox`

The SVG `viewBox` **is** the camera. Keyframe it in story time:

```js
// camera keyframes: {t0, t1, from:[x,y,w,h], to:[x,y,w,h], ease}
function cameraAt(t) { /* interpolate between keyframes */ }
render(t, params) {
  const c = cameraAt(t);
  stage.setAttribute("viewBox", `${c.x} ${c.y} ${c.w} ${c.h}`);
  ...
}
```

- **Zoom in** = shrink viewBox around the focus point (interpolate center
  toward the object, not just size — keep the subject framed).
- **Pan** = translate viewBox along the flow direction (follow the packet).
- **Focus pull** = zoom in + blur the far layer slightly (see §4).
- Rules: one camera move at a time; moves are 500–900 ms with ease-in-out;
  **no camera motion while a caption must be read** — move, then hold.
- Text safety: text scales with viewBox, so zoom depth is limited by minimum
  label size (compute: smallest label × zoom ≤ legible ⇒ clamp).

## 2. Scene transitions (cuts with continuity)

- Scenes = top-level `<g>` groups; visibility + opacity from `t` (pure).
- **Cut** on step boundaries (stepping feels like filming). Prefer
  **match cuts**: the object that carries continuity (the device, the packet)
  stays in the same screen position across the cut.
- **Crossfade** (300–450 ms) for same-place time passage; **slide** for spatial
  progress (along the story's dominant axis); **iris/blackout** reserved for
  entering the exception scenario.
- Never fade the focal object below legibility mid-move.

## 3. Easing philosophy

- UI/one-shot motions (enter, exit, emphasis pop): ease-out, 250–450 ms.
- Camera: ease-in-out, 500–900 ms — the eye forgives slow camera, not jerky.
- **Physics-true motion stays linear**: constant-velocity packets, rotating
  fields, clocks. Easing lies about physics; use it only on starts/stops of
  transport (a packet "departs" eased, then cruises linear).
- No bounce/elastic in technical content — they read as comedy.

## 4. Depth & lighting (2.5D without Three.js)

- **Layered composition**: background (stage, environment) → mid (conduits,
  infrastructure) → data layer (packets, values) → foreground HUD (captions,
  readouts). Assign each story actor a layer; effects respect layers
  (glow on data layer only).
- **Depth of field (fake)**: static blur on the background layer
  (`feGaussianBlur` once at build), extra opacity drop when the camera focuses
  elsewhere. Never blur the data layer.
- **Parallax**: during pans, background translates at 0.3–0.5× camera delta —
  compute from the same camera value (still deterministic).
- **Lighting**: cinematic dark stage (deep blue/graphite) with luminous data
  (see visual-design.md tokens). Light direction consistent (pick top-left or
  top); "power on" moments get a light sweep; "active" conductors glow.
- **Vignette**: one radial-gradient overlay ≤ 12% darkening at corners —
  focuses the eye without hiding content. Skip on light theme.

## 5. Composition rules

- Rule of thirds for the hero object; leave lead room in the direction of
  motion.
- Scale contrast: the hero at least 2× any secondary element in its shot.
- Readouts/HUD live at fixed screen positions (outside the camera group!)
  — HUD must not zoom with the world, or numbers become unreadable.
  Implementation: HUD in a separate SVG/group with its own fixed viewBox.

## 6. 2D vs 3D

Go 3D (Three.js) only when the knowledge is genuinely spatial 3D (package
stack-up, 3D field geometry). Everything in protocol/electronics teaching so
far is expressible in 2.5D — which is cheaper, sharper, and keeps text
crisp. Choosing 3D for looks is a gate failure, not a feature.

## 7. Checklist before implementation

- [ ] camera keyframes listed per shot in the motion storyboard
- [ ] every move derivable from `(t, params)`; no CSS animation for story motion
- [ ] captions/HUD fixed relative to screen, not world
- [ ] minimum text size verified at maximum zoom-out
- [ ] transitions aligned to step boundaries; match cut objects identified
- [ ] dark stage + glow tokens applied; light theme still legible
