# Benchmark Report: &lt;name&gt;（v2.1.0）

> 每个 Benchmark 一份；评分规则见 benchmarks/visual-scoring.md；填写实测量，禁止追填。
> 双门禁：技术门禁（validate_* / 浏览器 / scrub 确定性）必须 PASS 后才进行视觉评分。

## 1. 设计说明（Art Direction）

| 字段 | 内容 |
|---|---|
| 知识点 | |
| 视觉等级 | L1 / L2 / L3 |
| 三方向比选 | A … / B … / C …（各一行：构图·镜头·对知识点的适配）→ **选中 X，理由** |
| Hero moment | |
| 场景表 | 见 motion storyboard（场景 ID/构图/镜头/时间/交互/结束状态） |

## 2. 技术依据

| 断言 | 标签 | 来源（§ 级） |
|---|---|---|

## 3. 技术门禁（真实输出）

| 检查 | 工具 | 结果 |
|---|---|---|
| 静态 HTML | validate_html.py | |
| 控制契约 | validate_animation.py | |
| 浏览器交互 + 确定性 | tests/browser/run_repo_benchmarks.mjs | |
| 官方规范 | skills-ref（SKILL.md 级） | |

## 4. 视觉评分（六维 0–100，权重见 visual-scoring.md）

| 维度 | 权重 | 得分 | 证据（截图/输出路径） |
|---|---:|---:|---|
| Technical Accuracy | 25% | | |
| Visual Creativity | 20% | | |
| Motion Design | 20% | | |
| Storytelling | 15% | | |
| Interaction | 10% | | |
| Code Quality | 10% | | |
| **加权总分** | | | （N/A 维度剔除后重算） |

阈值：TA≥90 / VC≥80 / MD≥80 / 总分≥85。评分者身份必填；AI 评分须标注。

## 5. 截图证据

initial / playing / mid / exception / reset / narrow-720（路径列表）。

## 6. 已知限制

- …
