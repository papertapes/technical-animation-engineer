# Benchmark Result — usb-transfer-types（v2.1.0）

Date: 2026-10-31 · 设计方向与分镜：[design 文档](../design/usb-transfer-types-design.md) · 评分规则：[visual-scoring.md](../visual-scoring.md)

## 1. 设计说明（Art Direction 比选摘要）

三方向比选：A. Scientific Instrument 帧时间轴（**选中**——传输类型的本质差异是时间行为）/ B. Kinetic Infographic（弃，无过程）/ C. 多剧场（弃，无法同屏对照节奏）。

## 2. 技术依据

- 四种传输类型定义与机制（§5.5 Control / §5.6 Isochronous / §5.7 Interrupt / §5.8 Bulk，章节标题已核）
- Control 三阶段（§8.5.3）；Bulk 带宽按需 + NAK 重试 + DATA0/1（ch.8）；bInterval 轮询（§5.7/§9.6.6）
- Iso：每帧预留、无握手、不重传（§5.6）；TEACHING：帧内事务位置为示意、FS 帧简化

## 3. 技术门禁（真实输出，2026-10-31）

| 检查 | 工具 | 结果 |
|---|---|---|
| 静态 HTML | scripts/validate_html.py | PASS（0 错误） |
| 控制契约 | scripts/validate_animation.py | PASS（0 错误 0 警告） |
| 浏览器交互（load/play/pause/step/scrub/scenario/reset/720px） | Playwright + Chromium（tests/browser/run_repo_benchmarks.mjs） | PASS，0 控制台错误 |
| Scrub 确定性（同一 t 两次 seek 状态一致） | 同上内置断言 | PASS |
| SKILL.md 官方校验（仓库级） | skills-ref 0.1.1 | PASS（no issues） |

## 4. 视觉评分（AI 自评——独立审查见 §6）

| 维度 | 权重 | 得分 | 证据 |
|---|---:|---:|---|
| Technical Accuracy | 25% | 94 | 证据表（本文件 §2）；§级引用 |
| Visual Creativity | 20% | 84 | 设计方向比选 + 舞台实现（截图 §5） |
| Motion Design | 20% | 88 | 运动语言六问逐项落实（motion-language.md） |
| Storytelling | 15% | 86 | hero moment 落点 + 场景推进 |
| Interaction | 10% | 84 | 契约全项 + 本文件交互清单 |
| Code Quality | 10% | 88 | 静态/契约/浏览器测试全绿；单 rAF + render(t) 纯函数 |
| **加权总分** | | **88.0** | 阈值：TA≥90 / VC≥80 / MD≥80 / 总分≥85 → **PASS** |

## 5. 截图证据

`benchmarks/results/screenshots/usb-transfer-types/`：
01-initial · 02-playing · 03-mid · 04-exception · 05-reset · 06-narrow-720（真实浏览器捕获）。

## 6. 独立视觉审查

**第一轮**（独立 AI 审查代理，18 张截图 + 3× 变焦复核）：12/20 FAIL（1 BLOCKER：全部泳道事务块文字超出色块宽度，'ISO DATA'被切成'SO DATA'；另 4 MAJOR）

**修复**：全部 MAJOR/BLOCKER 已修复——B3 文字改短+色块按标签自适应宽度+警告/错误块白色文字+暗态对比修正；
B2 PID 标注移入专属间隙（缩放时下方层整体下移 30px）；截图脚本修复（异常场景现在推进到故障节拍后捕获）。
第二轮复核结论见下方追记。

**最终判定汇总**：B3 12→15/20 PASS；节拍。

**第二轮复核（逐项变焦验证）**：BLOCKER 确认修复（'SETUP→ACK'/'STATUS'/'POLL'/'BULK DATA0+ACK'/'ISO DATA' 全部完整可读）；焦点引导 1→2、设计观感 1→2、字幕同步 1→2；四种调度节奏确认真实可辨。**最终判定：15/20 PASS-WITH-MINOR**（残留 1 分项均为设计选择：单幕常驻、预建图表，非缺陷）。

## 7. 已知限制

- 未展示周期性带宽预算与 split 事务；帧数 4 为示意；交互式带宽计算器列为后续。


## 追记：第二轮复核详情

**第一轮**：12/20 FAIL（BLOCKER：全部事务块文字超出色块；4 MAJOR）。

**修复**：标签改短 + 色块按标签自适应宽度 + 警告/错误块白色文字 + 暗态对比修正 + 尺规注记独立成行 + POLL 裁切修复 + 异常截图对齐 Iso 节拍。

**第二轮复核（逐项变焦验证）**：BLOCKER 确认修复（'SETUP→ACK'/'STATUS'/'POLL'/'BULK DATA0+ACK'/'ISO DATA' 全部完整可读）；焦点引导 1→2、设计观感 1→2、字幕同步 1→2；四种调度节奏确认真实可辨。**最终判定：15/20 PASS-WITH-MINOR**（残留 1 分项均为设计选择：单幕常驻、预建图表，非缺陷）。

自动回归注记：第二轮回归：B3 12→15/20。