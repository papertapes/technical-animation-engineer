"""SKILL.md frontmatter：真 YAML 解析（PyYAML）+ 官方 skills-ref 校验器（可导入时）+ 规范约束。"""
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def load_meta():
    import yaml
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---")[1])

class TestYamlMetadata(unittest.TestCase):
    def test_frontmatter_is_valid_yaml(self):
        try:
            import yaml  # noqa
        except ImportError:
            self.skipTest("PyYAML 未安装（pip install pyyaml）")
        meta = load_meta()
        self.assertIsInstance(meta, dict)

    def test_required_fields_and_constraints(self):
        meta = load_meta()
        self.assertIn("name", meta)
        self.assertIn("description", meta)
        name = str(meta["name"])
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, ROOT.name)
        d = str(meta["description"])
        self.assertLessEqual(len(d), 1024)
        self.assertTrue(any(k in d.lower() for k in
                            ("use this", "use when", "use for", "when the user")))

    def test_official_validator(self):
        try:
            from skills_ref.validator import validate
        except ImportError:
            self.skipTest("skills-ref 未安装（pip install skills-ref）")
        res = validate(ROOT)
        self.assertEqual(res, [], "官方校验器问题: %s" % (res,))

if __name__ == "__main__":
    unittest.main()
