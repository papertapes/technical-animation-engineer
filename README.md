# Technical Animation Engineer

An [Agent Skill](https://agentskills.io/) for AI agents: design, build, audit,
and test **technically correct, interactive HTML/SVG/JavaScript teaching
animations** for engineering topics — network protocols (USB, EtherCAT, BLE,
Wi‑Fi), embedded systems (FOC, motor control, FreeRTOS, DMA, PWM, SPI/I2C/UART),
computer architecture, electronics, and beyond.

> Core principle: **Technical Accuracy First. Visual Quality Second.**
> Every claim shown in an animation carries an evidence tag
> (`SPEC` / `VENDOR` / `CHIP` / `SDK` / `TEACHING`); unverifiable claims are
> release blockers.

## What's in this repository

| Path | Purpose |
|---|---|
| `SKILL.md` | Entry point: gated workflow (analyze → storyboard → validate → implement → QA), evidence rules, unified control contract, reference loading map |
| `agents/openai.yaml` | OpenAI Codex UI metadata (Codex-specific extension, optional) |
| `references/` | 10 on-demand documents: animation taxonomy, technical accuracy, storyboard method & tutorial audit, SVG techniques, timeline control, visual design, interaction design, accessibility, testing, visual review |
| `assets/` | Templates: storyboard, animation spec, validation report |
| `scripts/` | `validate_skill.py` · `validate_html.py` · `validate_animation.py` (Python ≥ 3.8, stdlib only) |

## Install

Copy the folder into any Agent Skills–compatible location:

```bash
# OpenAI Codex (project scope — reads .agents/skills/ from the repo root)
cp -r technical-animation-engineer  <your-repo>/.agents/skills/

# Claude Code (personal scope)
cp -r technical-animation-engineer  ~/.claude/skills/

# Claude Code (project scope)
cp -r technical-animation-engineer  <your-repo>/.claude/skills/
```

## Verify the installation

```bash
cd technical-animation-engineer
python scripts/validate_skill.py .
# expected: Result: PASS (0 errors, 0 warnings)
```

Optional: Node.js enables inline-JS syntax checking in `validate_html.py`;
Playwright enables browser-level test suites (dev-time only).

## Use

Trigger it naturally in your agent:

- *"Create an animation that teaches USB enumeration."*
- *"Audit the animations in this HTML tutorial before changing anything."*
- *"This EtherCAT page says the master polls each slave — check that against
  the standard and fix the model."*
- *"Turn this static register-map diagram into an interactive explainer."*

The skill enforces: storyboard before code, evidence tagging for every
technical claim, a unified `data-tae-*` control contract (play/pause, step,
reset, speed, timeline, scenario) with a pure `render(t, params)` and one
requestAnimationFrame timing source, plus automated validation.

## About the larger project

This skill is the core of a larger project that includes five example
animations (one per animation type), three benchmark cases (EtherCAT
"processing on the fly", USB 2.0 enumeration, FOC Clarke/Park), a
Playwright browser test suite, and the underlying research. These companion
materials are maintained in the author's local project and may be published
separately.

## License

- **Code** (`scripts/`): [MIT](LICENSE)
- **Documentation** (`SKILL.md`, `references/`, `assets/`): [CC BY 4.0](LICENSE-DOCS)
- Third-party items: none shipped (see the main project's THIRD_PARTY_NOTICES.md)

---

## 中文说明

**Technical Animation Engineer** 是一个开放的 [Agent Skill](https://agentskills.io/)：
让 AI 代理能够设计、构建、审查并测试**技术正确、可交互**的 HTML/SVG/JavaScript
教学动画，覆盖网络协议（USB、EtherCAT、BLE、Wi-Fi）、嵌入式系统（FOC、电机控制、
FreeRTOS、DMA、PWM、SPI/I2C/UART）、计算机体系结构、电子学等领域。

> 核心原则：**技术正确性优先，视觉效果其次。**
> 动画中出现的每个技术结论都带证据标签（`SPEC` / `VENDOR` / `CHIP` / `SDK` /
> `TEACHING`），未核实的内容禁止发布，教学简化必须在页面上明示。

### 包含内容

| 路径 | 用途 |
|---|---|
| `SKILL.md` | 入口：门禁式工作流（分析 → 分镜 → 技术验证 → 实现 → QA）、证据规则、统一控制契约、参考文档加载地图 |
| `references/` | 10 篇按需加载的参考文档：动画类型、技术正确性、分镜方法与教程审计、SVG 技术、时间轴控制、视觉设计、交互设计、无障碍、测试、视觉审查 |
| `assets/` | 模板：分镜表、动画规格、验证报告 |
| `scripts/` | 三个纯标准库 Python 校验脚本：结构 / HTML / 动画契约 |
| `agents/openai.yaml` | OpenAI Codex 专属 UI 元数据（可选） |

### 安装

```bash
# OpenAI Codex（项目级，读取仓库根的 .agents/skills/）
cp -r technical-animation-engineer  <你的仓库>/.agents/skills/

# Claude Code（个人级）
cp -r technical-animation-engineer  ~/.claude/skills/

# Claude Code（项目级）
cp -r technical-animation-engineer  <你的仓库>/.claude/skills/
```

### 验证安装

```bash
cd technical-animation-engineer
python scripts/validate_skill.py .
# 预期输出：Result: PASS (0 errors, 0 warnings)
```

需要 Python ≥ 3.8（仅标准库）；可选：Node.js（JS 语法检查）、Playwright（浏览器测试，仅开发时使用）。

### 使用方式

在你的 AI 代理里用自然语言触发即可，例如：

- “创建一个讲解 USB 枚举的动画。”
- “先审计这个 HTML 教程里的所有动画，形成审计报告后再动手改。”
- “这个 EtherCAT 页面把从站处理写成了主站轮询——对照标准检查并修正。”
- “把这张静态寄存器图变成可交互的讲解页面。”

Skill 会强制执行：先分镜后编码、每个技术结论带证据来源、统一
`data-tae-*` 控制契约（播放/暂停、单步、重置、倍速、时间轴、场景）+
纯函数 `render(t, params)` + 单一 requestAnimationFrame 时间源，以及自动化验证。

### 许可证

- **代码**（`scripts/`）：MIT，见 [LICENSE](LICENSE)
- **文档**（`SKILL.md`、`references/`、`assets/`）：CC BY 4.0，见 [LICENSE-DOCS](LICENSE-DOCS)
- 未随附任何第三方资产（第三方研究与开发工具记录在主项目的 THIRD_PARTY_NOTICES.md）
