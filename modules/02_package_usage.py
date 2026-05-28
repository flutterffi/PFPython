"""Module lesson 02: package-level imports and object reuse."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython import LearnerProfile, build_banner


def main() -> None:
    learner = LearnerProfile(name="Grace", goal="packages", study_days=21)
    print(build_banner("Package Usage"))
    print(learner.summary())


if __name__ == "__main__":
    main()
