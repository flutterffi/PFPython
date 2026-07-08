"""Project 07 app entry: package-based backend application demo."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from backend_app.api import create_app


app = create_app()


def main() -> None:
    print("App main demo")
    print("=" * 13)
    print(app)
    print("\nIf FastAPI is installed, this object becomes a real ASGI app.")
    print("Suggested next step: move toward uvicorn app_main:app --reload")


if __name__ == "__main__":
    main()
