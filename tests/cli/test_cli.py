import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "privscan", "--help"],
        capture_output=True,
        text=True,
    )

    # help should exit with code 0
    assert result.returncode == 0

    combined = (result.stdout or "") + (result.stderr or "")

    # verify core help behavior
    assert "privscan" in combined
    assert "--help" in combined
