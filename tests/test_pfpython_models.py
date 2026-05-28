"""Tests for pfpython.models."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.models import LearnerProfile


def test_learner_profile_summary() -> None:
    learner = LearnerProfile(name="Plato", goal="Python", study_days=12)
    assert learner.summary() == "Plato is practicing Python for 12 days."


def main() -> None:
    test_learner_profile_summary()
    print("test_pfpython_models.py passed.")


if __name__ == "__main__":
    main()
