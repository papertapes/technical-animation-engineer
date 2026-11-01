# Third-Party Notices

**随仓库分发的产物（SKILL.md、references/、assets/、examples/、benchmarks/、scripts/、tests/）不含任何第三方代码、图片、字体或素材。** 全部页面为手写 HTML/CSS/JS/SVG（系统字体、无 CDN、无构建）。

## 开发时工具（不随产物分发）

| 工具 | 许可证（2026-10-31 复核） | 用途 |
|---|---|---|
| Playwright + Chromium | Apache-2.0 | tests/browser 真实浏览器测试 |
| Python 3.8+ / Node.js ≥18 | PSF / MIT | 测试与校验脚本 |
| skills-ref 0.1.1（pip，官方参考校验器） | Apache-2.0 | test_yaml_metadata.py（可导入时自动启用） |
| PyYAML | MIT | test_yaml_metadata.py 真 YAML 解析 |

## 研究过的项目（未使用其代码/素材）

D3 (ISC) · GSAP（**非 OSI**：自定义"no charge"许可，禁止打包进本仓库再分发）· Motion (MIT) · Manim Community (MIT) · SVG.js (MIT) · Three.js (MIT) · Mermaid (MIT) · Playwright (Apache-2.0)。许可证均于 2026-10-31 通过 GitHub LICENSE 端点 + npm registry 复核；方法、结论与来源链接见 SOURCES.md。

## 规则

新增第三方内容必须：许可证兼容且经官方文本复核 → 记录（项目/作者/许可证/版本/范围/核查日期）→ 保留版权声明；来源不明即排除。不得将第三方素材置于本仓库 MIT 覆盖之下。
