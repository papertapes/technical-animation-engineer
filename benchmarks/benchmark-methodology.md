# Benchmark Methodology

基准 = 用本 Skill 完整工作流（十步）构建、并用两道门禁 + 本评分体系验证的教学动画。
方法与设计要求见 `references/benchmark-design.md`；技术事实一律带 § 级引用（USB 事实
对照 USB-IF 官方文档核实，来源与日期见 SOURCES.md）。

## 流程

1. 选知识点 → Step 1–4（理解/叙事/艺术指导三比选/分镜）。
2. Step 5 高保真原型（独立 HTML，单文件零构建）。
3. Step 6–7 双向检查：视觉审查（十问）+ 技术验证（validate_* / 浏览器 / scrub 确定性）。
4. 截图取证：initial / playing / mid / exception / reset / 720px（runner 自动）。
5. 评分：visual-scoring.md 六维；结果与证据写入 `results/<name>.md`。
6. 集成与回归（如接入宿主教程）。

## 当前基准集

| 基准 | 主题 | 等级 | 结果 |
|---|---|---|---|
| usb-enumeration | 插入→复位→枚举→Configured | L3 | `results/usb-enumeration.md` |
| usb-packet-structure | 波形→包→字段爆炸（实时 CRC） | L3 | `results/usb-packet-structure.md` |
| usb-transfer-types | 四种传输的调度节奏 | L3 | `results/usb-transfer-types.md` |
