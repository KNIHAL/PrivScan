import re
from privscan.detectors.secrets import SecretDetector
from privscan.rules.models import Rule


def test_secret_detector_finds_match():
    rule = Rule(
        id="TEST_SECRET",
        category="secrets",
        regex=re.compile("secret123"),
        severity="high",
        description="test secret",
    )

    detector = SecretDetector([rule])
    results = detector.detect("my secret123 is here")

    assert len(results) == 1
    assert results[0]["rule_id"] == "TEST_SECRET"
