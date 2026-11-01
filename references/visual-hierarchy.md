# Visual Hierarchy

Information hierarchy is the pre-condition for focus: the viewer must be able
to answer "what am I looking at, what does it belong to, what detail is
available" without hunting. Three levels, enforced everywhere.

## The three levels

| Level | Content | Treatment |
|---|---|---|
| **L1 — Act** | the scene title / current question | largest type, screen-anchored HUD, appears with the scene cut |
| **L2 — Object** | the actors and their names | medium; distinct per semantic role (data/control/ok/error/wait/active) |
| **L3 — Detail** | byte values, bit grids, parameters, evidence lines | smallest; visible on demand (click/inspect) or when current |

Rules:
- At any instant, **at most one element per level** may be emphasized; one
  element total may carry the focal glow.
- Emphasis = size OR weight OR light OR isolation — pick two, never four.
- De-emphasis is active, not accidental: non-current objects get explicit
  reduced opacity (0.35–0.5) or desaturation, so focus reads as a decision.
- Hierarchy survives the camera: zooming must not promote a background detail
  above the HUD; HUD is screen-anchored.

## Channel discipline (how meaning maps to visual channels)

| Channel | Carries | Never carries |
|---|---|---|
| Position | topology, grouping, flow order | decoration |
| Color (semantic tokens) | role: data / control / ok / error / wait / active | random variety |
| Size / weight | magnitude, current focus | everything important at once |
| Light (glow/sweep) | activation events, current focus | permanent state |
| Motion | change, causality, direction | presence |

A value must appear on exactly one primary channel (plus text). If the same
fact is encoded three ways "for clarity", the frame has no hierarchy.

## Reading-order audit (do it on every scene)

1. Blur the frame mentally — what survives first? (must be the L1/L2 focus)
2. Squint — do the three levels separate into three visual planes?
3. Follow the caption — is the captioned object the most emphasized thing
   in frame? If not, the frame or the caption is wrong.
4. Check the exception state: does the error treatment outrank everything
   (it should, briefly), then settle back?

## Hierarchy failures (gate-visible)

- Flat frames: 10 elements at equal weight (Q3/Q5 fail).
- Inverted frames: byte-level detail brighter than the mechanism it belongs to.
- Orphan emphasis: a glow whose caption left two steps ago.
- HUD competition: readouts styled as hot as the focal object.
