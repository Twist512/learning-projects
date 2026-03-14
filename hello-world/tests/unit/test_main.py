from unittest.mock import patch

from src.main import hello_world


class TestHelloWorld:
    """Unit tests for hello_world function."""

    def test_hello_world_returns_string(self):
        """Verify hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)

    def test_hello_world_contains_hello(self):
        """Verify hello_world message contains Hello World."""
        result = hello_world()
        assert "Hello World" in result

    def test_hello_world_contains_oliver(self):
        """Verify hello_world message contains Oliver."""
        result = hello_world()
        assert "Oliver" in result

    def test_hello_world_uses_env_app_name(self):
        """Verify app name is pulled from environment variable."""
        with patch.dict("os.environ", {"APP_NAME": "TestApp"}):
            result = hello_world()
            assert "TestApp" in result

    def test_hello_world_uses_env_app_env(self):
        """Verify app environment is pulled from environment variable."""
        with patch.dict("os.environ", {"APP_ENV": "testing"}):
            result = hello_world()
            assert "testing" in result
