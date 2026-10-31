# Visual Storytelling

The design layer that separates a diagram-that-moves from a *teaching film*.
Fill [assets/visual-concept-template.md](../assets/visual-concept-template.md)
**before any layout or code**. The concept is reviewed like a storyboard: a
weak concept is cheaper to fix than a finished page.

## 1. The six questions (answer in writing)

1. **Hero moment** — what is the single most worth-showing visual instant of
   this knowledge point? (The instant where the mechanism *becomes visible*:
   the working counter cascading slave by slave; the dq frame snapping onto
   the rotating vector; the pull-up voltage tipping the hub into detection.)
   Every animation needs at least one; build the timeline to land it.
2. **Narrative** — how does the principle translate into a story? (A frame
   *travels*; a field *snaps* into alignment; a request is *refused and
   retried*.) State the story in one sentence a student could repeat.
3. **First sight** — what should the learner see before pressing anything?
   The initial frame must already orient: actors, stage, question.
4. **Attention direction** — how are close-up, zoom, cut and emphasis used to
   steer the eye? One focal point at a time; motion draws the eye — so motion
   must appear exactly where the explanation is.
5. **Continuity** — how do steps connect? Reuse positions, keep moving
   objects alive across cuts, let the camera travel instead of teleporting.
6. **Escape from box-and-arrow** — which *other* visual encodings can carry
   the content? (see §3)

## 2. Scene grammar (shot structure that teaches)

A technical story usually wants 3–5 shots:

| Shot | Job | Camera |
|---|---|---|
| Establish | the stage: actors, question, scale | wide, brief (≤ 2 steps) |
| Mechanism | the close-up where the knowledge lives | zoom in; slow down here |
| Consequence | what the mechanism causes (state change, data arriving) | follow the motion |
| Exception | failure/retry/timeout variant | cut hard — difference should feel different |
| Resolution | end state; what the learner can now explain | settle, hold |

Cut points align with step boundaries (so stepping = cutting). The camera
never moves during a caption that needs stable reading — move first, talk after.

## 3. Encodings beyond box-and-arrow

Boxes and arrows are fine for *structure*; they are lazy as *motion*. Vary by
meaning:

| Meaning | Better-than-a-box encoding |
|---|---|
| Data in flight | glowing packet with trail; particle stream whose density/speed encodes rate |
| Electricity / signal | traveling pulse along a conductor; waveform trace; voltage-plane color |
| Sequence / protocol | message ribbon laid down over time (a growing tape), not repeated arrows |
| State | lit floor in a tower; changing backdrop; badge morph |
| Quantity | bar/scale that breathes with the value; particle count |
| Structure | exploded view; layer separation; cutaway |
| Time | camera-locked scope with sweeping cursor; tape counter |

A metaphor is allowed if it is **labeled and does not mislead**: a wire drawn
as a pipe is fine — as long as real constraints (shared bus, half-duplex,
timing) are stated where they matter. The moment a metaphor contradicts the
mechanism (e.g., data "grabbed" by the master when the standard says the
frame streams through), the metaphor loses.

## 4. Attention & hierarchy rules

- One focal point per beat; dim/de-emphasize everything else (opacity, desaturation).
- Zoom = "the answer lives here". Use it at the mechanism shot, not everywhere.
- Motion contrast: when something important moves, stop what isn't.
- Captions adjacent to the focus; the caption and the glow land together.
- Never rotate or blur text; never let the camera outpace readability.

## 5. Level declaration

Declare L2 or L3 in the concept (see SKILL.md levels). Justify in one line
why this knowledge deserves it, and what the L2/L3 elements contribute to
*understanding*, not decoration. The visual quality gate will check exactly
that claim.
