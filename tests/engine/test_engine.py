import re
from pathlib import Path

from privscan.engine.engine import ScanEngine
from privscan.detectors.secrets import SecretDetector
from privscan.rules.models import Rule


def test_engine_adds_location_info(tmp_path: Path):
    test_file = tmp_path / "app.py"
    test_file.write_text("x = 1\napi_key = 'secret123'")

    rule = Rule(
        id="API_KEY",
        category="secrets",
        regex=re.compile("secret123"),
        severity="high",
        description="api key found",
    )

    engine = ScanEngine(SecretDetector([rule]))
    results = engine.scan_path(tmp_path)

    assert results[0]["line"] == 2
    assert results[0]["column"] == 12
    assert "api_key" in results[0]["line_text"]
