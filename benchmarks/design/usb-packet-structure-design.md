# 设计说明 — Benchmark 2: USB 2.0 Packet Structure（v2.1.0）

## Art Direction 比选

| 方向 | 表现 | 结论 |
|---|---|---|
| A. Scientific Instrument | 示波器+总线波形+字段读出器 | **选中**：包的本体就是波形，仪器视角让"模拟域↔结构域"的变换成为叙事核心 |
| B. Cinematic Dark Laboratory | 爆炸图特写 | 并入（结晶→爆炸即特写节奏） |
| C. Technical Editorial | 静态字段表 | 弃（丢失位宽比例与波形来源） |

## Motion Storyboard（8 步）

scope（波形+圈选）→ crystallize（结晶+SYNC 节拍）→ **explode（hero：按位宽比例分离）**
→ tour-pid（取反校验特写）→ tour-crc（校验器）→ tour-eop（SE0）→ reassemble → fly-ack。

## 实时 CRC（本 Benchmark 的核心技术点）

CRC 引擎按 §8.3.5 原文逐字实现（seed 全 1；高位置 0；若 高位⊕数据位=1 则异或
G(X)=00101B（CRC5）/1000000000000101B（CRC16）；CRC 取反后 MSb first 发送）。
验证：残差性质对任意数据恒等于规范值（CRC5=01100B，§8.3.5.1；CRC16=1000 0000 0000 1101B
=0x800D，§8.3.5.2），50+ 随机向量通过；CRC-16/USB 另与目录校验值一致
（"123456789"→0xB4C8）。交互：编辑 ADDR/ENDP/载荷 hex → CRC 位串与残差实时重算；
Binary/Hex 切换。

## 已知限制

- 波形为概念示意（TEACHING）；DATA 载荷长度缩略显示；HS SYNC=32 位以字幕标注（图示 8 位）。
- 高速 PING/NYET 等特殊包未纳入（课程 U09 数据范围）。
