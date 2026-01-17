from pathlib import Path
from privscan.scanner.reader import read_file


def test_read_file(tmp_path: Path):
    file = tmp_path / "test.txt"
    file.write_text("hello world")

    content = read_file(file)
    assert content == "hello world"
