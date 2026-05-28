"""Package entry point for `python -m pfpython`."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.banner import build_banner
from pfpython.practice import build_practice_plan


def main() -> None:
    print(build_banner("PFPython"))
    print("Today's suggestion:")
    for item in build_practice_plan():
        print(f"- {item}")


if __name__ == "__main__":
    main()
