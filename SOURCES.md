# Sources — 技术事实与设计参考（核查日期 2026-10-31）

全部技术事实带证据标签（SPEC/VENDOR/CHIP/SDK/TEACHING），未核实内容为发布阻塞项。
本 Skill 未复制任何第三方内容；许可证复核记录见 THIRD_PARTY_NOTICES.md。

## [1] 官方技术标准（USB 事实的一手依据）

| 来源 | 用于 | 状态 |
|---|---|---|
| USB 2.0 Specification, Rev 2.0 — USB-IF | 三个 USB Benchmark 全部事实：设备状态（§9.1.1/Fig 9-1）、复位（§7.1.7.5/Fig 7-29）、控制事务（§8.5.3/Fig 8-36）、CRC 算法与残差（§8.3.5 原文逐字实现）、传输类型（§5.5–5.8，章节标题已核）、端点描述符（§9.6.1/9.6.6） | VERIFIED（本地官方文档逐页核对） |

## [2] 官方厂商/组织文档

| 来源 | 用于 | 状态 |
|---|---|---|
| agentskills.io 规范页 + GitHub agentskills/agentskills | SKILL.md frontmatter 规范（六字段、name=目录名、渐进式加载） | VERIFIED |
| developers.openai.com/codex/skills | agents/openai.yaml 字段与发现路径 | VERIFIED |

## [3] 学术/教学研究

Mayer & Moreno 2003（free PDF, uky.edu）；Tversky/Morrison/Bétrancourt 2002（IJHCS，定性结论经多源交叉）；Mayer & Chandler 2001（ERIC EJ638751）；NSW CESE 2017；Noetel et al. 2022；Karich 2014；de Jong et al. 2013 —— 完整清单见主项目 SOURCES.md。VERIFIED（定性）。

## [4] 开源项目（只研究思想，未复制代码/素材）

D3 (ISC) / GSAP (自定义"no charge"许可，非 OSI) / Motion (MIT) / Manim Community (MIT) / SVG.js (MIT) / Three.js (MIT) / Web Animations API (平台) / Mermaid (MIT) / Playwright (Apache-2.0) —— 许可证均于 2026-10-31 经 GitHub LICENSE 端点与 npm registry 复核；复核方法与使用范围见 THIRD_PARTY_NOTICES.md。
