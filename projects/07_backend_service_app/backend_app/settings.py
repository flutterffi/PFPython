"""Package settings layer for the backend practice app."""

import os


def load_settings() -> dict[str, object]:
    return {
        "app_name": os.getenv("PFPYTHON_BACKEND_APP_NAME", "PFPython Backend Package"),
        "default_topic": os.getenv("PFPYTHON_BACKEND_TOPIC", "python"),
        "max_results": int(os.getenv("PFPYTHON_BACKEND_MAX_RESULTS", "3")),
    }


def main() -> None:
    print("Package settings demo")
    print("=" * 21)
    print(load_settings())


if __name__ == "__main__":
    main()
