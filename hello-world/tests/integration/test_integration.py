import subprocess
import sys


class TestIntegration:
    """Integration tests — runs the full application end to end."""

    def test_app_runs_successfully(self):
        """Verify the app runs without errors."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0

    def test_app_outputs_hello_world(self):
        """Verify the app prints Hello World to stdout."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main"],
            capture_output=True,
            text=True
        )
        assert "Hello World" in result.stdout

    def test_app_outputs_oliver(self):
        """Verify the app prints Oliver to stdout."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main"],
            capture_output=True,
            text=True
        )
        assert "Oliver" in result.stdout
