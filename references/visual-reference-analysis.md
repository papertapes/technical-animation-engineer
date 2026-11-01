# Visual Reference Analysis

How to study external visual work **legally and usefully** — analysis of
design methods only, original re-implementation always.

## 1. What may be studied

Public design work and tools: Behance / Dribbble / Awwwards portfolios,
Manim Community renders, science documentaries, chip-vendor visualizations,
oscilloscope/analyzer UIs, kinetic-type reels, open-source science animation
projects. Study: composition, color relations, motion character, camera
grammar, scene transitions, data representation, information layering,
interaction patterns, rhythm.

## 2. Hard rules

- 分析思想、规律、方法 —— 严禁复制代码、提取素材、重制受版权保护的完整动画、
  伪造原创性、删除第三方版权声明。
- 公开可访问 ≠ 授权使用。Any asset (image/font/icon/audio) requires a license
  check; unverified = excluded (`UNVERIFIED` blocks release).
- If a third-party asset IS used (with license), it must NOT be placed under
  this project's MIT umbrella — record it in THIRD_PARTY_NOTICES.md with its
  own license and scope.
- Prefer studying *methods* over mimicking *looks*: a reference teaches "why
  this composition clarifies this content", not "copy this gradient".

## 3. The reference ledger (mandatory format)

Every consulted external reference gets one row in the project's
`SOURCES.md` (or a visual-reference ledger section):

| Field | Example |
|---|---|
| 作者/组织 | Manim Community |
| 原始链接 | https://docs.manim.community/... |
| 作品名称 | "ValueTracker + updaters pattern" (documentation) |
| 参考日期 | 2026-10-31 |
| 参考的设计理念 | single mutable state driving visuals per frame |
| 是否使用第三方代码/素材 | 否（仅思想；实现为本项目原创） |
| 许可证 | MIT（若涉及代码） |

No row = no reference may influence the design. AI agents must not fabricate
ledger rows: only record what was actually fetched/read in the session, with
real URLs.

## 4. Analysis method (per reference)

1. **Deconstruct to technique, not style**: name the composition, hierarchy
   levels, motion character, camera grammar, transition logic.
2. **Find the load-bearing choice**: which single visual decision makes the
   content understandable? (That is what is worth borrowing.)
3. **Map to our vocabulary**: express the finding as a rule or token in our
   system (composition-and-layout.md / motion-language.md / art-direction.md).
4. **Original re-implementation**: implement with our tokens and engine; the
   result must survive a side-by-side "did we copy?" test.

## 5. Session example (already recorded in SOURCES.md)

- Manim Community (MIT): scene→acts→steps decomposition and the
  value-tracker/updaters pattern → re-derived as this skill's
  `render(t, params)` rule (no Manim code used).
- Tversky/Morrison/Bétrancourt 2002: apprehension & congruence principles →
  encoded as the taxonomy's animate-vs-static decision rules.
- MDN Web Animations docs: pause/scrub model considerations → our story clock
  remains a single rAF loop (deterministic) with WAAPI only for one-shots.
