"""控制契约测试：运行 scripts/validate_animation.py，断言 0 错误。"""
import subprocess
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestAnimationControls(unittest.TestCase):
    def test_examples_follow_contract(self):
        examples = sorted((ROOT / "examples").glob("*/index.html"))
        self.assertTrue(examples)
        for page in examples:
            with self.subTest(page=page.name):
                r = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_animation.py"), str(page)],
                                   capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

if __name__ == "__main__":
    unittest.main()
