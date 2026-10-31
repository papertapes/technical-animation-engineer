# Unified Timeline & Control System

All interactive animations built with this skill share one control
architecture. Its purpose: **pause/resume is exact, stepping is precise,
reset is complete, scrubbing never corrupts state, and captions never
desync.**

## 1. State model

Two kinds of state, never mixed:

- **Timeline-derived state** — everything that changes as the story plays
  (packet position, working counter, current step, byte values in flight).
  Computed from timeline position `t` (story-time, ms). Never mutated
  directly by user input.
- **User parameters** — only changed through explicit inputs (duty cycle,
  frequency, amplitude, scenario). They persist across seek and pause; only
  **Reset** restores their defaults (unless a scenario preset defines them).

## 2. The rendering rule (the single most important rule)

```js
function render(t, params) {
  // compute EVERYTHING from t and params:
  // object positions, highlighted states, buffer contents,
  // counters, displayed numbers, caption index
}
```

`render(t, params)` must be a **pure function** of timeline position and
parameters. Consequences:

- Pause/resume is exact (position `t` fully describes the frame).
- Scrubbing/stepping just re-runs `render` — no incremental corruption.
- `Reset` is `render(0, defaults)`.
- The numbers on screen and the graphics are computed from the same state —
  no decorative fake numbers.

Cost: you must implement state as a function of time rather than an
accumulating sequence of mutations. This is the core discipline of the
skill. For event-like moments (a packet "arriving"), define step boundaries
and let `render` decide which side of the boundary `t` is on.

## 3. One timing source

```js
let rafId = null, lastTick = null;
function loop(now) {
  const dt = now - lastTick; lastTick = now;
  t = Math.min(t + dt * speed, DURATION);   // story-time advance
  render(t, params);
  if (t < DURATION && playing) rafId = requestAnimationFrame(loop);
  else if (t >= DURATION) setPlaying(false); // end of story = paused at end
}
```

- Exactly **one** `requestAnimationFrame` loop per page. **No `setInterval`**
  for animation logic (a stray interval keeps running while paused and
  desyncs state).
- `speed` multiplies story-time, not wall time. Changing speed mid-play must
  not jump the position (it doesn't — position derives from accumulated
  story-time).
- When the tab is hidden, rAF pauses automatically — resume logic must
  tolerate the resulting large `dt` (clamp `dt` to e.g. 100 ms).

## 4. Control contract

| Control | Attribute | Behavior |
|---|---|---|
| Play/Pause | `data-tae-action="play-pause"` | toggles; label/aria-label reflects next action |
| Step Forward | `data-tae-action="step-fwd"` | `seek(nextBoundary(t))`; exactly one step |
| Step Backward | `data-tae-action="step-back"` | `seek(prevBoundary(t))` |
| Reset | `data-tae-action="reset"` | `t=0`, `params=defaults`, paused, scenario cleared |
| Speed | `data-tae-action="speed"` | select with e.g. 0.5× / 1× / 2× |
| Scenario | `data-tae-action="scenario"` | sets param preset, `seek(0)` |
| Timeline | `data-tae-timeline` (input range) | maps slider ↔ `t`; on input, `seek(v)` |
| Caption | `data-tae-caption` | shows caption of the step containing `t` |

Not every animation needs every control — omit deliberately and record the
decision in the animation spec's control matrix. Play/pause and Reset are
required for anything with a timeline.

Steps are declared once as data (id, start, caption, log) and drive both
stepping and captions:

```js
const STEPS = [
  { id: "attach",   start: 0,    caption: "Device attached: D+ pull-up detected." },
  { id: "reset",    start: 800,  caption: "Host drives SE0 ≥ 10 ms — bus reset." },
  // ...
];
```

## 5. Test/debug API

Expose a single global for tests and power users:

```js
window.__TAE__ = {
  duration: DURATION, position: () => t, playing: () => playing,
  steps: STEPS.map(s => ({ id: s.id, start: s.start })),
  play, pause, seek, step: n => seekBySteps(n), reset,
  setParams: p => { params = { ...params, ...p }; render(t, params); },
};
```

`validate_animation.py` checks its presence; the Playwright suite drives it.

## 6. Minimal page skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>… — knowledge point</title>
  <style> /* theme tokens, layout, reduced-motion, dark mode */ </style>
</head>
<body>
  <main>
    <h1>…</h1>
    <section class="tae-stage" aria-label="Animation stage">
      <svg viewBox="0 0 900 420" role="img" aria-labelledby="stage-title">
        <title id="stage-title">…</title>
        <!-- semantic groups: devices, data, signals, state -->
      </svg>
    </section>
    <p class="tae-caption" data-tae-caption aria-live="polite"></p>
    <div class="tae-controls" role="group" aria-label="Playback controls">
      <button data-tae-action="reset"      aria-label="Reset">⟲</button>
      <button data-tae-action="step-back"  aria-label="Step backward">−1</button>
      <button data-tae-action="play-pause" aria-label="Play">▶</button>
      <button data-tae-action="step-fwd"   aria-label="Step forward">+1</button>
      <select data-tae-action="speed" aria-label="Playback speed">
        <option value="0.5">0.5×</option><option value="1" selected>1×</option>
        <option value="2">2×</option>
      </select>
      <input type="range" data-tae-timeline min="0" max="1000" value="0"
             aria-label="Timeline position">
    </div>
    <footer class="tae-evidence">Evidence: SPEC … · TEACHING: …</footer>
  </main>
  <script>
    // ONE rAF loop; render(t, params) pure; window.__TAE__ exposed
  </script>
</body>
</html>
```

## 7. Common bugs this design prevents

| Bug | Cause | Prevented by |
|---|---|---|
| Resume drifts or double-speeds | two timers / interval not cleared | one rAF, dt-based |
| Scrub leaves stale visuals | incremental mutations | pure `render(t, params)` |
| Reset misses a variable | hand-rolled reset lists | reset = render(0, defaults) |
| Caption shows step n+1 | caption driven by its own timer | caption index from `t` |
| End state unrecoverable | interval died at end | rAF loop stops but seek works |
| Speed change jumps position | speed applied to position | speed multiplies dt only |
