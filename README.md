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
