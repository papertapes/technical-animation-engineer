# Motion Language

The grammar of movement. `motion-graphics.md` is the *effects catalog*; this
file is the *language system* — when a movement happens, how fast, in what
order, and what it must not imply. Every technique below must answer the six
questions before use.

## The six questions (apply to every motion decision)

1. 什么场景适合使用？ — the scene type that justifies it.
2. 它表达什么技术信息？ — the quantity/state/order it encodes.
3. 运动速度和节奏如何决定？ — the real value or convention it maps to.
4. 是否可能产生技术误导？ — the lie it could tell and the guard.
5. 如何通过交互控制？ — play/pause/step/scrub/parameter that governs it.
6. 如何进行视觉验收？ — what the reviewer checks on the timeline.

## Technique table

| Technique | 适合场景 | 表达的信息 | 速度/节奏依据 | 误导风险与护栏 | 交互控制 | 验收要点 |
|---|---|---|---|---|---|---|
| Ease In | 启动/离开舞台 | 从静止投入运动 | 场景节拍（300–450ms） | 混淆为物理加速；物理匀速运动不用 | 播放/暂停 | 起步柔和、随后线性 |
| Ease Out | 进入焦点 | 到达与安定 | 同上 | 到达"漂移"过久 | 同上 | 末速趋零 |
| Anticipation | 动作前的预备（插头回抽再插入） | 因果的准备阶段 | 幅度 ≤ 主运动 20% | 夸张变成卡通；幅度标注 | scrub 可见全过程 | 观众能预判主动作 |
| Follow Through | 到达后的余量（灯带越过一格回弹） | 能量衰减 | ≤ 2 个衰减周期 | 暗示真实回弹物理 | 同上 | 不与数据变化冲突 |
| Overlapping Action | 多对象依次启动 | 传播时序 | 依次延迟 = 传播时序（缩放标注） | 顺序错误 = 教错协议 | 单步逐步可见 | 顺序与规范一致 |
| Secondary Motion | 主对象运动带出的从属（标签跟动、线缆抖动） | 主从关系 | 幅度 ≤ 主运动 30% | 喧宾夺主 | 跟随主运动 | 焦点仍在主对象 |
| Motion Path | 沿真实通路移动 | 通路形状与长度 | 匀速 = 物理速率（缩放标注） | 路径暗示错误拓扑 | scrub 全程 | 路径与拓扑一致 |
| Morphing | 结构变化（空闲→包） | 域变换 | 一个节拍完成 | 形状无语义 | 暂停对比两端 | 两端状态都正确 |
| Signal Propagation | 导体上的因果传播 | 传播方向与时序 | 缩放后的物理速率 | 方向反了=教反 | 单步可见波前 | 方向+时序正确 |
| Particle Flow | 通道活动度 | 速率/密度 | 粒子速率∝真实速率（缩放） | 密度无意义=噪声 | 暂停冻结 | 数量-速率映射成立 |
| Data Stream | 字节/字流动 | 载荷内容 | 每珠=真实字节 | 珠数与字节数不符 | scrub | 珠数=标注字节数 |
| Light Sweep | 上电/启用瞬间 | "激活"事件 | ≤700ms 单次 | 变成常驻循环 | 场景重放可触发 | 只在事件步出现 |
| Dynamic Highlight | 当前讲解对象 | 焦点 | 250ms 内到位 | 多焦点=无焦点 | 随单步切换 | 同一时刻仅一个 |
| Camera Pan | 空间推进 | 位置关系 | 500–900ms ease-in-out | 文字出框 | scrub 可回看 | 文本完整可读 |
| Camera Zoom | 机制特写 | "答案在这里" | 同上，落定后保持 | 缩放中读字 | 同上 | 最小字号达标 |
| Camera Focus | 主次切换 | 焦点转移 | 与 caption 同步 | 焦点漂移 | 同上 | 焦点唯一 |
| Scene Transition | 阶段/幕切换 | 结构边界 | 300–450ms | 掩盖状态跳变 | 步进=切幕 | 幕边界=步边界 |
| Layer Separation / Exploded View | 内部结构 | 组成与位宽 | 沿声明轴，一个节拍 | 分离轴与真实结构不符 | 点击/参数控制 | 层内容与规范一致 |
| Timeline Animation | 总线调度 | 时间片占用 | 真实比例（帧/微帧缩放标注） | 时间片长度失真 | 时间轴 scrub | 占用比例正确 |

## Rhythm system

- **Beat**: one step = one beat (2–4 s). A beat may contain sub-motion but one
  *new* idea.
- **Phrase**: 3–5 beats forming a scene; scenes end on a settled frame.
- **Restraint**: at most 2 simultaneous motions in frame; everything else is
  still or ambient.
- **Continuity**: positions persist across steps; objects re-enter only when
  the story re-introduces them.
- **Reduced motion**: ambient and anticipation/follow-through disabled; story
  advances by steps; nothing essential is motion-only.

## Acceptance hooks

The visual quality gate scores motion (Q6) using this table: a reviewer picks
any three motions and asks the six questions — two unanswered questions fail
the item.
