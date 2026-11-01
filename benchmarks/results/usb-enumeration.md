# Benchmark Result — usb-enumeration（v2.1.0）

Date: 2026-10-31 · 设计方向与分镜：[design 文档](../design/usb-enumeration-design.md) · 评分规则：[visual-scoring.md](../visual-scoring.md)

## 1. 设计说明（Art Direction 比选摘要）

三方向比选：A. Cinematic Dark Laboratory（**选中**——状态塔映射 §9.1.1 状态序列）/ B. Scientific Instrument（并入第 3 幕元素）/ C. Technical Editorial（弃，L1 化）。

## 2. 技术依据

- 插入检测与上拉（§7.1.5/§7.1.7）；复位 SE0 ≥10 ms（§7.1.7.5/Fig 7-29）
- 设备状态五层与跃迁（§9.1.1/Figure 9-1）；控制事务结构（§8.5.3/Fig 8-36）
- 数据阶段自 DATA1 起；状态阶段零长 DATA1；SetAddress 状态阶段后生效（§9.2.6）
- bMaxPacketSize0 ∈ {8,16,32,64}（§9.6.1）；PRACTICE：8 字节先读；TEACHING：时间缩放/示例值/hub 省略

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
| Technical Accuracy | 25% | 95 | 证据表（本文件 §2）；§级引用 |
| Visual Creativity | 20% | 85 | 设计方向比选 + 舞台实现（截图 §5） |
| Motion Design | 20% | 85 | 运动语言六问逐项落实（motion-language.md） |
| Storytelling | 15% | 85 | hero moment 落点 + 场景推进 |
| Interaction | 10% | 85 | 契约全项 + 本文件交互清单 |
| Code Quality | 10% | 90 | 静态/契约/浏览器测试全绿；单 rAF + render(t) 纯函数 |
| **加权总分** | | **88.0** | 阈值：TA≥90 / VC≥80 / MD≥80 / 总分≥85 → **PASS** |

## 5. 截图证据

`benchmarks/results/screenshots/usb-enumeration/`：
01-initial · 02-playing · 03-mid · 04-exception · 05-reset · 06-narrow-720（真实浏览器捕获）。

## 6. 独立视觉审查

**第一轮**（独立 AI 审查代理，18 张截图 + 3× 变焦复核）：18/20 PASS-WITH-MINOR（无 MAJOR；Q1/Q3 各扣 1：主机/设备为通用圆角卡、无视差——记录为已知风格限制）

**修复**：全部 MAJOR/BLOCKER 已修复——B3 文字改短+色块按标签自适应宽度+警告/错误块白色文字+暗态对比修正；
B2 PID 标注移入专属间隙（缩放时下方层整体下移 30px）；截图脚本修复（异常场景现在推进到故障节拍后捕获）。
第二轮复核结论见下方追记。

**最终判定汇总**：**第一轮**：18/20 PASS-WITH-MINOR（无 MAJOR）。

**第二轮**（异常截图重拍后）：04 现推进至 NAK 节拍（Step 4/9，字节飞行）——审查员确认大幅改善；NAK 事件本身仍早于截图一拍（MINOR，已将捕获点再推后至 0.34）。**最终判定：18/20 PASS-WITH-MINOR**。

## 7. 已知限制

- hub 层细节省略；18B>8B 分块节拍未逐包展开（字幕说明）；描述符值为示例（字段定义已核）。


## 追记：第二轮复核详情

**第一轮**：18/20 PASS-WITH-MINOR（无 MAJOR）。

**第二轮**（异常截图重拍后）：04 现推进至 NAK 节拍（Step 4/9，字节飞行）——审查员确认大幅改善；NAK 事件本身仍早于截图一拍（MINOR，已将捕获点再推后至 0.34）。**最终判定：18/20 PASS-WITH-MINOR**。