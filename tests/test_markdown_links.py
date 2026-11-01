"""全仓库 Markdown 相对链接测试：所有 .md 内的相对链接必须能解析到真实文件。"""
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

class TestMarkdownLinks(unittest.TestCase):
    def test_all_relative_links_resolve(self):
        broken = []
        md_files = (list(ROOT.glob("*.md")) + list(ROOT.glob("references/*.md")) +
                    list(ROOT.glob("assets/*.md")) + list(ROOT.glob("benchmarks/**/*.md")) +
                    list(ROOT.glob("examples/**/design.md")))
        for md in md_files:
            for m in LINK.finditer(md.read_text(encoding="utf-8")):
                target = m.group(1)
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                path = target.split("#")[0]
                if path and not (md.parent / path).exists():
                    broken.append("%s -> %s" % (md.name, target))
        self.assertEqual(broken, [], "断链: " + "; ".join(broken))

if __name__ == "__main__":
    unittest.main()
