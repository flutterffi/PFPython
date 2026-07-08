"""Project 07 config: settings for a backend-style practice app."""

import os


def load_settings() -> dict[str, object]:
    return {
        "app_name": os.getenv("PFPYTHON_BACKEND_APP_NAME", "PFPython Backend Service"),
        "default_topic": os.getenv("PFPYTHON_BACKEND_TOPIC", "python"),
        "log_level": os.getenv("PFPYTHON_BACKEND_LOG_LEVEL", "INFO"),
        "max_results": int(os.getenv("PFPYTHON_BACKEND_MAX_RESULTS", "3")),
    }


def main() -> None:
    settings = load_settings()
    print("Config demo")
    print("=" * 11)
    print(settings)


if __name__ == "__main__":
    main()
