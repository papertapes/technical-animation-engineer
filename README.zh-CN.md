# Technical Animation & Motion Design Director（中文说明）

一个开放的 [Agent Skill](https://agentskills.io/)：让 AI 以**专业动效设计**水准构建、
审计与升级技术教学动画——协议（USB/EtherCAT/BLE）、嵌入式（FOC/FreeRTOS/DMA/PWM）、
体系结构与电子学。

> 原则：**技术准确性优先；视觉质量第二——但同样是硬性要求。**
> 每个技术结论带证据标签（SPEC/VENDOR/CHIP/SDK/TEACHING），未核实内容禁止发布。

## 仓库内容

| 路径 | 用途 |
|---|---|
| `SKILL.md` | 入口：十步强制工作流、证据规则、统一控制契约、加载地图 |
| `references/`（20 篇） | 动画类型、**艺术指导**、视觉叙事、动效目录、电影化镜头、构图、运动语言、信息层级、技术准确性、分镜与审计、SVG 技术、时间轴、视觉设计、交互、无障碍、测试、视觉审查、**视觉质量门禁**、外部参考分析、基准设计 |
| `examples/` | 三个可运行 USB Benchmark（见下方展示区） |
| `benchmarks/` | 评分方法 + 设计文档 + 结果与截图 |
| `tests/` | Python 测试套件 + Playwright 浏览器测试 + CI |

## 安装

```bash
cp -r technical-animation-engineer <你的仓库>/.agents/skills/   # Codex
cp -r technical-animation-engineer ~/.claude/skills/            # Claude Code
```

## 验证

```bash
python scripts/validate_skill.py .     # PASS
python tests/run_tests.py              # 全部测试（浏览器测试需 Node+Playwright）
```

## 三个 Benchmark（截图见 benchmarks/results/screenshots/）

- **usb-enumeration**：插入→供电→复位→控制事务→Configured；状态塔+事务珠链+描述符字段表。
- **usb-packet-structure**：波形→结晶→按位宽爆炸；**实时规范 CRC**（§8.3.5 原文实现），
  Binary/Hex 切换，ADDR/ENDP/载荷可编辑。
- **usb-transfer-types**：同一时间轴上四种传输的调度节奏对照（Control/Interrupt/Bulk/Iso）。

## 许可证

代码 MIT（LICENSE）；文档 CC BY 4.0（LICENSE-DOCS）。无第三方素材随仓库分发。
