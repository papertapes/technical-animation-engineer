# Validation Report: &lt;Animation ID / page path&gt;

| Field | Value |
|---|---|
| Date | |
| Validator | tool + version, and/or reviewer (human / AI agent) |
| Environment | browser + version, OS, viewport sizes |
| Verdict | PASS / FAIL / CONDITIONAL (list conditions) |

## 1. Static checks — `validate_html.py`

Paste the tool's per-file result (errors / warnings). Every ERROR must be
resolved or justified before continuing.

## 2. Animation contract — `validate_animation.py`

Controls present (play/pause, reset, step, speed, timeline), single timing
source, no anti-patterns. Paste tool result.

## 3. Runtime checks — real browser

| Check | Result | Evidence (screenshot / log path) |
|---|---|---|
| Page opens with zero console errors / page errors | | |
| Play starts the animation | | |
| Pause freezes it; resume continues exactly (no drift) | | |
| Step Forward = exactly one defined step | | |
| Step Backward returns to previous step | | |
| Reset restores initial state (incl. parameters) | | |
| Speed control changes pace without breaking state | | |
| Timeline scrub matches animation state | | |
| Scenario switch resets and reconfigures | | |
| Parameter changes update graphics **and** computed numbers | | |

## 4. State-machine tests (if applicable)

- initial state correct
- every legal transition verified
- illegal transition attempt does not corrupt state
- exception branch reachable and displayed
- final state correct

## 5. Visual review — screenshots

Screenshots at t=0, middle, end, exception state; at 1280px and 720px widths.

- [ ] no text overflow or truncation
- [ ] no unintended element overlap
- [ ] arrow directions match the described flow
- [ ] color semantics consistent (data / control / error / active)
- [ ] contrast readable in both themes
- [ ] caption and animation state in sync
- [ ] animation pace readable (not too fast to follow)

A visual review cannot be claimed from code reading alone: attach screenshots.

## 6. Technical accuracy review

- Evidence Table from storyboard.md reviewed row by row
- any `UNVERIFIED` claim present? (release blocker)
- any `TEACHING` simplification that could be mistaken for real behavior?
  (must be labeled on screen)

## 7. Verdict & Follow-ups

| Item | Owner | Status |
|---|---|---|
| | | |

> Honesty rule: record what was actually tested and what was not. An
> unchecked box stays unchecked; never fill the report aspirationally.
