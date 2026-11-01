"""可访问性静态测试：lang、控件 aria、键盘操作、reduced-motion。"""
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestAccessibility(unittest.TestCase):
    def test_pages_meet_a11y_basics(self):
        for page in sorted((ROOT / "examples").glob("*/index.html")):
            with self.subTest(page=page.name):
                s = page.read_text(encoding="utf-8")
                self.assertRegex(s, r'<html lang="')
                self.assertIn("prefers-reduced-motion", s)
                self.assertIn('tabindex="0"', s)
                self.assertIn("ArrowRight", s)
                for m in re.finditer(r'<button[^>]*data-tae-action="([^"]+)"[^>]*>', s):
                    tag = m.group(0)
                    has_label = ("aria-label" in tag) or re.search(r">[^<]", tag)
                    self.assertTrue(has_label,
                                    "%s: 控件缺少可访问名称: %s" % (page.name, tag))

if __name__ == "__main__":
    unittest.main()
