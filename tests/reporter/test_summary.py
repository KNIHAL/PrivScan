from privscan.reporter.summary import SummaryReporter


def test_summary_reporter():
    findings = [
        {"severity": "high"},
        {"severity": "low"},
        {"severity": "high"},
    ]

    reporter = SummaryReporter()
    output = reporter.render(findings)

    assert "HIGH" in output
    assert "2" in output
    assert "LOW" in output
    assert "LOW" in output and "1" in output

    
