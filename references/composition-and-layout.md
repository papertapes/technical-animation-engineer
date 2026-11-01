# Composition & Layout

Composition is how the frame answers "where should the eye go, and in what
order". Pick the composition **per scene** from the knowledge content; a
project may use several. The default failure mode is "everything laid out
left-to-right in one row" — that is a composition choice that was never made.

## The catalog

| Composition | Frame grammar | Use it when (technical examples) |
|---|---|---|
| Rule of Thirds | subject on third lines/intersections | establishing shots; a device that will act later sits on a third |
| Center Composition | subject dead-center, symmetrical support | the mechanism *is* the single story (a packet crystallizing) |
| Symmetrical | mirrored halves | master↔device reciprocity, differential pairs, request/response |
| Asymmetrical | dominant zone + counterweight | host-heavy narratives (host initiates everything) |
| Layered | fg/mg/bg planes with distinct treatments | protocol stacks, encapsulation, any depth story |
| Split-Screen | hard vertical/horizontal divide, optionally synced cursors | before/after, two sides of an exchange, old/new behavior |
| Exploded View | parts translate apart along stated axes | packet/register/connector anatomy |
| Close-Up | subject fills frame, context cropped | bit-level fields, pin contact, electrical detail |
| Macro View | far wider than needed to establish scale | "you are here" — system vs component |
| Cutaway | outer shell partially removed | device internals (ESC, PHY, FIFO) |
| Spatial Depth | explicit z ordering with size/blur/position shifts | scheduling hierarchies, memory maps |
| Parallax | layers move at different rates during camera moves | depth during pans (never on data labels) |
| Focal Point | one element isolated by light/size/motion | the current explanation target (mandatory per beat) |
| Information Hierarchy | 3-level text/object hierarchy: title → label → detail | every scene; define before styling |

## Layout system (non-negotiables)

- Semantic layout first: the *relationships* (who talks to whom, what contains
  what) must be readable from positions alone.
- Reading order = attention order = step order. If step 2 is about the right
  side, don't park step 1's focus on the left margin.
- Reserve stable regions: HUD/captions never move; the stage composition may
  change but its anchor points shouldn't jump between steps.
- Spacing scale (4/8/12/16/24/32 px) and a 3-level type scale; margins > gaps
  > padding — emptiness is what makes focus possible.
- Cropping: composition may crop *empty* space, never mid-glyph. Text is
  either fully in frame or fully out (fade the object instead).
- Every scene states its composition in the motion storyboard; the visual
  quality gate checks that adjacent scenes don't all use the same one.

## Anti-patterns

- The left-to-right conveyor for everything.
- Decorative asymmetry that fights the semantic symmetry of an exchange.
- Centered everything (no hierarchy).
- Twelve equal-weight boxes — that is a data table pretending to be a diagram.
