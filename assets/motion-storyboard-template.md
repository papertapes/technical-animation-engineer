# Motion Storyboard: &lt;Animation ID&gt;

> Shot-level plan bridging the visual concept and the code (workflow step 3).
> Companion: `visual-concept.md` (story) and `storyboard.md` (facts/evidence).
> Camera and effects listed here must end up inside `render(t, params)`.

## Global

| Field | Value |
|---|---|
| Story timeline | total steps; step boundaries (story-time ms) |
| Camera rig | viewBox keyframes per shot (from → to, easing) |
| Stage theme | cinematic dark / standard |
| Effects earned | list each with its "encodes quantity Y" line (anti-stack rule) |
| HUD plan | fixed readouts/captions (screen-anchored, outside camera group) |

## Shot sheet

| # | Shot ID | Steps (ids) | Start–End (t) | Camera (viewBox from→to / hold) | Layers in/out | Effects used | On-screen data | Caption |
|---|---|---|---|---|---|---|---|---|
| 1 | establish | | 0–2000 | wide hold | stage, actors | ambient only | question text | … |
| 2 | mechanism | | | zoom → focus point | data layer up | glow hand-off | live values | … |

One row per shot; step ids must match the story storyboard exactly (stepping
= cutting).

## Keyframe details (per moving element)

| Element | Keyframes (t → state) | Easing | Encodes |
|---|---|---|---|
| | | | |

## Transition plan

| Between shots | Type (cut / match-cut / crossfade / slide / iris) | Carrier of continuity | Duration |
|---|---|---|---|

## Interaction hooks per shot

| Shot | Interactive affordance | What it teaches |
|---|---|---|
| | | |

## Reduced-motion plan

What changes under `prefers-reduced-motion`: ambient loops off, camera moves
replaced by cuts, story advances via steps — nothing essential lost.

## Pre-flight checklist

- [ ] every effect has its "encodes Y" line (no stacking)
- [ ] captions readable at every camera position (min text size at max zoom-out)
- [ ] HUD screen-anchored
- [ ] hero moment lands early enough to be reached
- [ ] transitions align with step boundaries; match-cut carriers named
- [ ] all camera/effects derivable from (t, params) — deterministic
