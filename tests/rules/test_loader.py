from privscan.rules.loader import RuleLoader


def test_rule_loader(tmp_path):
    rules_file = tmp_path / "test.yml"
    rules_file.write_text(
        """
- id: TEST_RULE
  category: secrets
  regex: "test123"
  severity: low
  description: test rule
"""
    )

    loader = RuleLoader(tmp_path)
    rules = loader.load()

    assert len(rules) == 1
    assert rules[0].id == "TEST_RULE"
