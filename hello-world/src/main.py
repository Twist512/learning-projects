import os

from dotenv import load_dotenv

from src.logger import get_logger

load_dotenv()

logger = get_logger(__name__)


def hello_world() -> str:
    """Return a hello world message using config from .env file."""
    app_name = os.getenv("APP_NAME", "App")
    app_env = os.getenv("APP_ENV", "unknown")
    message = (
        f"Hello World from {app_name} and Oliver! "
        f"Running in {app_env} environment."
    )
    logger.info(message)
    return message


def main():
    """Main entry point for the application."""
    logger.info("Application starting...")
    result = hello_world()
    print(result)
    logger.info("Application finished.")


if __name__ == "__main__":
    main()
