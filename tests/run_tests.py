"""测试运行器：python tests/run_tests.py"""
import sys
import unittest
from pathlib import Path

def main():
    suite = unittest.defaultTestLoader.discover(str(Path(__file__).resolve().parent),
                                                pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    print("\ntests: %d, failures: %d, errors: %d, skipped: %d" %
          (result.testsRun, len(result.failures), len(result.errors), len(result.skipped)))
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(main())
