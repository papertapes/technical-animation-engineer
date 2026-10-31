# Visual Quality Gate

An acceptance gate **independent of the technical gate**. The technical gate
asks "is it right?"; this one asks "is it worth watching — and does the
visual design make the knowledge easier to understand?" A page passes only
when both pass.

## When it runs

After implementation, before "done" is claimed — and **again after any
restyling pass**. It requires screenshots: the gate cannot be run by reading
code. Reviewer should not be the page's author when possible.

## The 10 questions (score each 0 / 1 / 2)

| # | Question | 0 | 2 |
|---|---|---|---|
| 1 | Is it still just boxes and arrows? | boxes+arrows only | structure rendered through the content's own imagery (packets, fields, traces, exploded layers) |
| 2 | Is there a visual narrative (hero moment, scene flow)? | one flat continuous diagram | declared hero moment lands; 3+ shots with distinct jobs |
| 3 | Dynamic layering? | everything same plane, same weight | depth/layering used; background recedes; data pops |
| 4 | Scene changes? | single static composition throughout | camera/scene changes tied to story beats |
| 5 | Visual focus guidance? | eye wanders; many equal elements | one focal point per beat; zoom/glow/dimming steer attention |
| 6 | Motion quality? | linear tween of position only | effects encode data (rate, state, energy); easing deliberate |
| 7 | Unnecessary static stretches? | long static holds with nothing changing | holds are purposeful (reading time); ambient life where relevant |
| 8 | Interactive exploration? | play/pause only | step/scrub/scenario/parameters/object inspection invite questions |
| 9 | Expressiveness overall? | generic template look | coherent designed look (stage, palette, typography, signature moment) |
| 10 | Comprehension gain? | visuals don't reduce effort | a learner can *see* the mechanism the caption describes |

**Threshold: ≥ 15/20 to pass; any question scored 0 blocks.** For an upgrade
task, also compute the old version's score — the new version must beat it by
**≥ 5 points**; otherwise iterate (§4).

## Hard rule — what does NOT count as an upgrade

The following alone are explicitly rejected as "upgraded":
background/color changes, font changes, rounded corners, shadows, plain
gradients, resizing boxes, recoloring arrows. An upgrade must show
substantive improvement in **at least one** of: animation narrative, motion
design, visual structure, or interactive experience — verified by the 10
questions and side-by-side shots.

## Comparison protocol (for upgrade tasks)

1. Fix the shot list: initial / 25% / 50% / 75% / end / exception / narrow.
2. Capture old and new at the same list, same viewport(s).
3. Produce a side-by-side sheet (old | new) per shot + one motion note line
   per shot ("old: box slides; new: propagation pulse leads the packet in").
4. Score both with the 10 questions; record both scores and the delta.
5. List technical-gate status for both (accuracy must not regress).

## Common failure patterns (pre-flight self-check)

- "Skin pass": new theme, same skeleton → Q1/Q2/Q9 still 0–1.
- Effect soup: every effect everywhere → Q5 fails (no focus).
- Camera drunk: constant motion, captions unreadable → Q5/Q10 fail.
- Ambient loops everywhere → reduced-motion violation, Q6 suffers.
- Hero moment announced in the concept but landing at 95% of a 30 s timeline
  → nobody reaches it; move it earlier or shorten the path.

## Sign-off

Record in the validation report: per-question scores, old/new delta, shot
sheet paths, reviewer identity, and the iterate-or-pass decision. Honesty
rule applies: a failed gate is recorded as failed until it actually passes.
