"""Skill 结构测试：运行 scripts/validate_skill.py 并断言 PASS。"""
import subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestSkillStructure(unittest.TestCase):
    def test_validate_skill_passes(self):
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py"), str(ROOT)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("PASS", r.stdout)

if __name__ == "__main__":
    unittest.main()
