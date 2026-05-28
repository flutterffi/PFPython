"""Engineering lesson 03: configuration from defaults and environment variables."""

from os import getenv


def main() -> None:
    app_mode = getenv("PFPYTHON_MODE", "practice")
    debug_flag = getenv("PFPYTHON_DEBUG", "false").lower() == "true"

    print(f"app_mode = {app_mode}")
    print(f"debug_flag = {debug_flag}")
    print("Try running this file after exporting different environment variables.")


if __name__ == "__main__":
    main()
