# Changelog

## [2.1.0] — 2026-10-31 · Motion Design Director

### Added
- 十步强制工作流（理解→叙事→艺术指导→分镜→高保真原型→视觉审查→技术验证→集成→回归→终审）。
- Art Direction Generator 与 6 个新 references（art-direction / composition-and-layout / motion-language / visual-hierarchy / visual-reference-analysis / benchmark-design）。
- 三个 USB Benchmark（examples/usb-enumeration · usb-packet-structure · usb-transfer-types），含设计文档与截图证据。
- benchmarks/（methodology + 六维评分 visual-scoring + results）。
- tests/ 九测试文件 + run_tests.py + GitHub Actions CI（.github/workflows/ci.yml）。
- 合规文件进仓库（SOURCES/THIRD_PARTY_NOTICES/ASSET_ATTRIBUTION）+ README.zh-CN.md。

### Fixed
- **P0**：SKILL.md description 未加引号 → 官方 skills-ref 校验失败（真 YAML 解析器发现，自写解析器曾漏过）；现已官方校验 PASS。
- 资产目录 3 处 `../../references/` 断链；仓库误跟踪 __pycache__（新增 .gitignore 并移除）。

## [2.0.0] — 2026-10-31
Motion Design 升级：视觉等级 L1–L3、视觉叙事/动效目录/电影化/独立视觉质量门禁、五模板。

## [1.0.0] — 2026-10-31
首个完整版本（技术准确性纪律、统一控制契约、五类型示例、三校验脚本）。
