"""真实浏览器交互测试（Playwright/Chromium）：委托 tests/browser/run_repo_benchmarks.mjs。"""
import subprocess
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tests" / "browser" / "run_repo_benchmarks.mjs"

class TestBrowserInteraction(unittest.TestCase):
    def test_benchmarks_in_browser(self):
        try:
            subprocess.run(["node", "--version"], capture_output=True, check=True)
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("Node.js 未安装")
        r = subprocess.run(["node", str(RUNNER)], capture_output=True, text=True,
                           cwd=str(RUNNER.parent))
        output = r.stdout + r.stderr
        if "ERR_MODULE_NOT_FOUND" in output:
            self.skipTest("playwright 未安装（cd tests/browser && npm i playwright）")
        self.assertEqual(r.returncode, 0, output[-2000:])

if __name__ == "__main__":
    unittest.main()
