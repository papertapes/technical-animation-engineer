# 设计说明 — Benchmark 3: USB 2.0 Transfer Types（v2.1.0）

## Art Direction 比选

| 方向 | 表现 | 结论 |
|---|---|---|
| A. Scientific Instrument | 总线帧时间轴 + 四条泳道 + 游标扫描 | **选中**：四种传输类型的本质差异是**时间行为**，只有时间轴能同时表达节奏差异 |
| B. Kinetic Infographic | 四色大数字对比卡 | 信息真实但无过程；调度是时间概念 | 弃（作为 summary 字幕补充） |
| C. Cinematic Dark Laboratory | 每类型一个小剧场 | 四个小剧场无法同屏对比节奏；镜头切换打散对照 | 弃 |

## 核心教学决策

**同一时间轴、四种节奏同屏对照**：Control 稀疏（三阶段一簇）、Interrupt 严格周期
（间隔参数实时改变轮询点）、Bulk 见缝插针（剩余带宽 + NAK 重试）、Iso 固定节拍
（每帧预留、无握手标注、CRC 错误直接丢弃）。异常下拉注入 bulk-NAK 与 iso-CRC-error
—— "可靠 vs 实时"的分野由画面直接呈现。

## 技术依据

§5.5 Control / §5.6 Isochronous / §5.7 Interrupt / §5.8 Bulk（章节标题已对照官方
PDF 核实）；Control 三阶段 §8.5.3；Bulk NAK 重试与 DATA0/1 交替（ch.8）；bInterval
轮询语义（§5.7、§9.6.6）。TEACHING：帧内事务位置/数量为示意（真实调度由主机策略
决定）；用 FS 帧演示（HS 微帧以字幕说明）。

## 已知限制

- 未展示周期性带宽预算计算与 split 事务。
- 帧数 4（示意）；交互式带宽计算器列为后续增强。
