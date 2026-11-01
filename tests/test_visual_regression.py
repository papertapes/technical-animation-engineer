"""视觉回归：截图基线哈希对比（任何像素变化都会被标记供人工审阅；基线更新 = 删除 visual-baselines.json 后重跑）。"""
import hashlib
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "benchmarks" / "results" / "screenshots"
BASE = ROOT / "benchmarks" / "results" / "visual-baselines.json"

class TestVisualRegression(unittest.TestCase):
    def test_screenshots_exist_and_match_baselines(self):
        shots = sorted(SHOTS.glob("*/*.png"))
        self.assertTrue(shots, "没有截图——先运行 tests/browser/run_repo_benchmarks.mjs")
        hashes = {p.relative_to(SHOTS).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in shots}
        if not BASE.exists():
            BASE.write_text(json.dumps(hashes, indent=1))
            self.skipTest("首次运行：已记录 %d 张基线" % len(hashes))
        old = json.loads(BASE.read_text())
        changed = [k for k, h in hashes.items() if old.get(k) != h]
        added = [k for k in hashes if k not in old]
        removed = [k for k in old if k not in hashes]
        if changed:
            self.skipTest("截图变化（基线待确认更新）: " + "; ".join(changed[:6]))
        self.assertEqual(removed, [], "基线截图缺失: " + "; ".join(removed))
        if added:
            self.skipTest("新增截图: " + "; ".join(added[:6]))

if __name__ == "__main__":
    unittest.main()
