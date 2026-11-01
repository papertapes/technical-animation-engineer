# Art Direction

Before any animation is designed, generate **2–3 clearly different visual
directions** and select one with a recorded reason (SKILL.md workflow step 3).
Three directions that differ only by accent color are one direction, not
three.

## 1. The five archetypes (start here, don't end here)

| Archetype | Stage & surfaces | Objects | Light | Motion signature | Best for |
|---|---|---|---|---|---|
| **A. Cinematic Dark Laboratory** | deep-navy void, instrument silhouettes, shallow "table" plane | precision-machined devices, glowing internals, cutaways | single key light + luminous data, strong vignette | slow deliberate camera, macro close-ups | mechanisms hidden inside hardware; insertion/assembly stories |
| **B. Scientific Instrument** | instrument face: scope grid, channel labels, measurement chrome | traces, cursors, fields-as-readouts, timing rulers | even "phosphor" glow, no theatrical shadow | sweep/cursor motion, live numbers, probing | signal-level knowledge, timing, protocols-as-measurements |
| **C. Technical Editorial** | paper/ink or dark print aesthetic, strong type grid, generous margins | flat diagrammatic objects with hairline strokes, numbered callouts | flat (no glow), hierarchy via weight/size | typographic reveals, step counters, tidy wipes | taxonomy/structure content, comparisons, reference material |
| **D. Blueprint / Schematic Draft** | drafting grid, construction lines, annotation layer | wireframe→solid build-up, dimension marks | monochrome + one accent | draw-on (stroke-dash reveal), dimension ticks | explaining *how something is built*, layered architecture |
| **E. Kinetic Infographic** | bold color fields, oversized numerals | proportional bars/areas, big counters | flat, high-contrast | scale/counter dynamics, compare-morphs | quantitative stories (bandwidth, overhead, timing budgets) |

## 2. Per-direction token spec (what a direction must define)

Each chosen direction is written down as tokens before layout:

1. 视觉主题 — one sentence naming the world ("a night-lab bench under a
   inspection lamp").
2. 设计理念 — what this style makes *inherently clear* for this knowledge.
3. 构图 — default composition per scene (see composition-and-layout.md).
4. 色彩 — 1 primary + 2 supporting + semantic set (data/control/ok/error/wait),
   fixed as CSS custom properties; contrast pairs verified for both themes.
5. 背景与空间层次 — background / mid / data / HUD layers and their treatment.
6. 技术对象表现法 — how devices, packets, fields, states are drawn (shape
   grammar), reusing the project's semantic color language.
7. 运动语言 — 3–5 signature moves (see motion-language.md); everything else
   stays quiet.
8. 镜头语言 — camera grammar for this direction (A: slow push-ins; B: none,
   cursor only; C: none; D: pan across the sheet).
9. 关键帧与转场 — the hero moment and how scenes cut (cuts on step boundaries).
10. 交互反馈 — hover/focus/selection treatment in this style.
11. 教学适用性 — the one-line claim the visual quality gate will score.

## 3. Selection procedure

1. Generate ≥ 3 directions that differ in **archetype or in structure**, not
   merely palette.
2. Score each against: knowledge fit (does the style expose the mechanism?),
   attention economy (does it add focus or noise?), cost (can it be built
   well in SVG/Canvas at this scope?), accessibility (contrast/reduced-motion).
3. Pick one; record the comparison table and the reason in the visual concept
   document. In autonomous mode pick the strongest teaching fit and record
   why the others lost.
4. The losing directions are not discarded work — they are the evidence of
   the "directions differ" requirement, and may be reused for sibling topics.

## 4. Anti-patterns

- Three palettes of the same dark-lab layout.
- Picking a direction because it looks expensive, then fighting it for clarity.
- Mixing archetypes mid-animation without a scene-level reason.
- Direction tokens defined in prose only — they must land as CSS custom
  properties or they will drift during implementation.
