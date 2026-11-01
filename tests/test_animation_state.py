"""动画状态架构静态测试：单一时间源、render(t,params)、__TAE__ API。"""
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestAnimationState(unittest.TestCase):
    def test_pages_follow_state_architecture(self):
        for page in sorted((ROOT / "examples").glob("*/index.html")):
            with self.subTest(page=page.name):
                s = page.read_text(encoding="utf-8")
                intervals = len(re.findall(r"\bsetInterval\s*\(", s))
                self.assertLessEqual(intervals, 1, "违反单一时间源")
                self.assertIn("requestAnimationFrame", s)
                self.assertIn("window.__TAE__", s)
                self.assertIn("render(", s)

if __name__ == "__main__":
    unittest.main()
