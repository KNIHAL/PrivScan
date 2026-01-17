import json
from privscan.reporter.json_reporter import JSONReporter


def test_json_reporter(tmp_path):
    output = tmp_path / "report.json"
    findings = [{"rule_id": "X", "severity": "high"}]

    reporter = JSONReporter()
    reporter.write(findings, output)

    data = json.loads(output.read_text())
    assert data["total_findings"] == 1
    
    
   

