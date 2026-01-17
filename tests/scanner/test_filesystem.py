from pathlib import Path
from privscan.scanner.filesystem import FileScanner


def test_scanner_ignores_env_and_report(tmp_path: Path):
    env_file = tmp_path / "env" / "a.py"
    report = tmp_path / "report.json"
    valid = tmp_path / "main.py"

    env_file.parent.mkdir()
    env_file.write_text("token = 'bad'")
    report.write_text("token = 'bad'")
    valid.write_text("print('ok')")

    scanner = FileScanner(tmp_path)
    results = list(scanner.scan())

    assert valid in results
    assert env_file not in results
    assert report not in results
