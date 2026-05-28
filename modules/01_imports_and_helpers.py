"""Module lesson 01: direct imports from the local package."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.banner import build_banner
from pfpython.models import LearnerProfile


def main() -> None:
    learner = LearnerProfile(name="Ada", goal="syntax", study_days=14)
    print(build_banner("Imports"))
    print(learner.summary())


if __name__ == "__main__":
    main()
