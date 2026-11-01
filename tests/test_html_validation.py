"""示例 HTML 静态验证：运行 scripts/validate_html.py，断言 0 错误。"""
import subprocess
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestHtmlValidation(unittest.TestCase):
    def test_examples_pass(self):
        examples = sorted((ROOT / "examples").glob("*/index.html"))
        self.assertTrue(examples, "examples/ 下没有 index.html")
        for page in examples:
            with self.subTest(page=page.name):
                r = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_html.py"), str(page)],
                                   capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

if __name__ == "__main__":
    unittest.main()
