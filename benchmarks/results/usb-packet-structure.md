# Benchmark Result — usb-packet-structure（v2.1.0）

Date: 2026-10-31 · 设计方向与分镜：[design 文档](../design/usb-packet-structure-design.md) · 评分规则：[visual-scoring.md](../visual-scoring.md)

## 1. 设计说明（Art Direction 比选摘要）

三方向比选：A. Scientific Instrument（**选中**——包的本体是波形，模拟域↔结构域变换即叙事）/ B. Cinematic（并入结晶→爆炸节奏）/ C. Editorial（弃）。

## 2. 技术依据

- 字段位宽（SYNC 8/32、PID 8、ADDR 7、ENDP 4、CRC5 5、CRC16 16、FrameNumber 11、EOP=SE0）
- PID 值与取反校验（Table 8-1）；CRC16 残差 1000 0000 0000 1101B、CRC5 残差 01100B（§8.3.5）
- CRC 引擎按 §8.3.5 原文逐字实现；残差性质经 50+ 随机向量验证（数据无关）；TEACHING：波形概念示意、载荷缩略

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
| Technical Accuracy | 25% | 97 | 证据表（本文件 §2）；§级引用 |
| Visual Creativity | 20% | 86 | 设计方向比选 + 舞台实现（截图 §5） |
| Motion Design | 20% | 87 | 运动语言六问逐项落实（motion-language.md） |
| Storytelling | 15% | 84 | hero moment 落点 + 场景推进 |
| Interaction | 10% | 92 | 契约全项 + 本文件交互清单 |
| Code Quality | 10% | 88 | 静态/契约/浏览器测试全绿；单 rAF + render(t) 纯函数 |
| **加权总分** | | **89.5** | 阈值：TA≥90 / VC≥80 / MD≥80 / 总分≥85 → **PASS** |

## 5. 截图证据

`benchmarks/results/screenshots/usb-packet-structure/`：
01-initial · 02-playing · 03-mid · 04-exception · 05-reset · 06-narrow-720（真实浏览器捕获）。

## 6. 独立视觉审查

**第一轮**（独立 AI 审查代理，18 张截图 + 3× 变焦复核）：18/20 PASS-WITH-MINOR（2 MAJOR：PID 标注与 ADDR 层叠印、英雄镜头取景）

**修复**：全部 MAJOR/BLOCKER 已修复——B3 文字改短+色块按标签自适应宽度+警告/错误块白色文字+暗态对比修正；
B2 PID 标注移入专属间隙（缩放时下方层整体下移 30px）；截图脚本修复（异常场景现在推进到故障节拍后捕获）。
第二轮复核结论见下方追记。

**最终判定汇总**：层下方间隙。

**第二轮**：发现修复回归——NAK 场景的取反标注仍叠在窄色块标签上（MAJOR）。

**修复二（最终）**：层名全部外置左侧（x=162 右对齐）、取值标注统一置于色块右侧——此类叠印从结构上消除；NAK 场景复检零叠印。**最终判定：18/20 PASS-WITH-MINOR**（残留 MINOR：NAK 包仅 3 个短层，画面偏空——与包的真实结构一致，记录为已知项）。

## 7. 已知限制

- 高速 PING/NYET/SPLIT 未纳入；HS SYNC=32 位以字幕标注；载荷长度缩略显示。


## 追记：第二轮复核详情

**第一轮**：18/20 PASS-WITH-MINOR（2 MAJOR：英雄镜头取景塌缩、PID 标注遮挡）。

**修复一**：等比取景 + 层下方间隙。

**第二轮**：发现修复回归——NAK 场景的取反标注仍叠在窄色块标签上（MAJOR）。

**修复二（最终）**：层名全部外置左侧（x=162 右对齐）、取值标注统一置于色块右侧——此类叠印从结构上消除；NAK 场景复检零叠印。**最终判定：18/20 PASS-WITH-MINOR**（残留 MINOR：NAK 包仅 3 个短层，画面偏空——与包的真实结构一致，记录为已知项）。

自动回归注记：第二轮回归：B2 18/20。