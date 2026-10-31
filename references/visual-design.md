# Visual Design System

Visual quality serves knowledge表达 — every rule below exists to make the
*content* easier to read, not the page prettier. Principles behind these
rules: coherence, signaling, spatial contiguity (see
[animation-taxonomy.md](animation-taxonomy.md) and project `SOURCES.md`).

## 1. Design tokens (CSS custom properties)

Every page defines these tokens once and uses them everywhere:

```css
:root {
  /* surfaces & text */
  --bg: #ffffff; --surface: #f5f7fa; --ink: #1f2933; --ink-dim: #52606d;
  --line: #cbd2d9;
  /* semantic */
  --c-data:    #2563eb;  /* data transfer / payload / packets */
  --c-control: #7c3aed;  /* control signals / requests / events */
  --c-ok:      #059669;  /* normal / success / active-good */
  --c-error:   #dc2626;  /* errors, timeouts, mismatches */
  --c-wait:    #d97706;  /* waiting / pending / NAK */
  --c-active:  #0d9488;  /* currently-acting object / focus of explanation */
  --highlight: #fde68a;  /* attention background */
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f1720; --surface: #17212b; --ink: #e6edf3; --ink-dim: #9fb0bf;
    --line: #33414e;
    --c-data: #60a5fa; --c-control: #c4b5fd; --c-ok: #34d399;
    --c-error: #f87171; --c-wait: #fbbf24; --c-active: #2dd4bf;
    --highlight: #7a5c10;
  }
}
```

- **The same semantic color means the same thing across all pages of a
  project.** Data is blue everywhere; control is violet everywhere.
- Meaning is never carried by color alone — pair with a label, shape, or
  outline style (accessibility.md).

## 2. Shape language (consistent object grammar)

| Role | Shape | Example |
|---|---|---|
| Device / block | rounded rectangle with header label | Host, Slave 1, DMA |
| Data unit | pill / small rect, `--c-data` fill, payload text inside | frame, descriptor byte |
| Signal / message | line or arrow, `--c-control`, labeled | request, token |
| State | rounded badge / node, border colored by status | Default, Blocked |
| Buffer cell | small square, fill opacity = occupancy | FIFO slots |

## 3. Emphasis conventions

- **Current focus of explanation:** thick `--c-active` outline or
  `--highlight` background — at most one such element at a time.
- **Past:** dimmed (opacity ~0.45). **Pending/not-yet:** ghost (dashed
  outline, low opacity). **Error:** `--c-error` + solid border + label.
- Don't bold everything. Hierarchy: size first, weight second; max two
  weight levels on screen.

## 4. Layout

- Regions: stage (SVG) on top, caption directly beneath it, controls under
  caption, parameters aside or below — the caption is *adjacent* to what it
  describes (spatial contiguity).
- Spacing scale: 4 / 8 / 12 / 16 / 24 / 32 px. Whitespace is free; crowding
  is expensive.
- Max content width ~1100 px; stage min-height stable across steps (no
  layout jumps when captions change length).
- Labels live on/near their objects, not in a faraway legend only; legends
  supplement, they don't replace direct labeling.

## 5. Typography

- System font stack (`system-ui, -apple-system, "Segoe UI", Roboto,
  "Helvetica Neue", Arial, "Noto Sans", sans-serif`) — zero webfont payload.
- Body ≥ 14 px; SVG labels ≥ 11 px effective size at minimum width.
- Monospace for byte values, registers, equations with numbers.
- Title states what is taught ("USB Enumeration — device states & control
  transfers"), not what is animated ("Cool animation #3").

## 6. Motion rules

- Story-time is scaled and the scale is stated ("1 step ≈ 8 ms real time");
  UI transitions (non-story) are ≤ 300 ms.
- Easing: `ease`/`ease-out` for UI; linear for position-vs-time in
  physics-true motion (a constant-velocity packet must not ease!).
- Decorative animation: none. Reduced motion: honored
  ([accessibility.md](accessibility.md)).

## 7. Arrows & direction

- Arrowheads on the receiving end; direction must match the described flow
  (this is checked in visual review — markers silently pointing the wrong
  way are a classic defect).
- Bidirectional exchanges use two offset arrows, not one double-headed one,
  when order matters.
- Return/response arrows get distinct style (dashed or thinner) from
  request arrows when the distinction is part of the lesson.

## 8. Anti-patterns

- Rainbow palettes, gradients-as-decoration, glow everywhere.
- Uniform gray-on-gray "sleek" pages where nothing is distinguishable.
- Bold + large + colored all at once (that's four kinds of emphasis doing
  one job).
- Ten colors where six tokens would do; ad-hoc hex values scattered in JS.
- Icons/emoji carrying technical meaning without labels.

## 10. Cinematic stage theme (for L2–L3 storytelling pages)

Beyond the standard light/dark document themes, L2–L3 pages may use a
**cinematic stage**: a dark, deep-blue/graphite canvas that lives *inside the
SVG stage only* (the surrounding document stays in the user's theme). This
makes luminous data — packets, pulses, glow — read like light on an
instrument.

```css
/* stage-scoped tokens; document chrome keeps normal theme */
.stage--cinematic { background: radial-gradient(120% 120% at 50% 30%, #10233a 0%, #0a1420 55%, #060c14 100%); }
.stage--cinematic .surface { fill:#13263a; stroke:#2a415c; }
.stage--cinematic .label   { fill:#b8c9dd; }
```

- Data = light: packets/pulses use the semantic colors at full saturation +
  glow; infrastructure is dim slate; text ≥ 4.5:1 against the stage.
- One vignette overlay (≤ 12% corner darkening) max; skip on light theme.
- HUD/readouts stay fixed (screen-anchored), high contrast, never blurred.
- The standard light/dark document themes remain the default for L1 and
  always remain available — cinematic stage is a story choice, recorded in
  the visual concept, not a global restyle.

## 11. Motion duration tokens

| Token | Duration | Use |
|---|---|---|
| `--t-enter` | 300–450 ms | element enters/leaves, emphasis pop |
| `--t-move` | 500–900 ms | camera pan/zoom, scene transition |
| `--t-sweep` | ≤ 700 ms | light sweep, power-on |
| ambient | 3–4 s loop | idle breathing/dash march (reduced-motion: off) |

Physics-true motion is excluded from tokens — it stays linear and true.

## 9. Verification

Both themes checked by screenshot review ([visual-review.md](visual-review.md));
contrast spot-checked (WCAG AA: text 4.5:1, graphics 3:1); `validate_animation.py`
warns when evidence tags or reduced-motion support are missing.
