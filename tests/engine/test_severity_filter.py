from privscan.engine.engine import ScanEngine
from privscan.detectors.secrets import SecretDetector


def test_severity_filter():
    engine = ScanEngine(SecretDetector([]))

    findings = [
        {"severity": "low"},
        {"severity": "medium"},
        {"severity": "high"},
    ]

    filtered = engine._filter_by_severity(findings, "high")
    assert len(filtered) == 1
    assert filtered[0]["severity"] == "high"
