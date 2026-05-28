"""Tests for pfpython.practice."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.practice import build_practice_plan


def test_practice_plan_has_steps() -> None:
    steps = build_practice_plan()
    assert len(steps) >= 4
    assert steps[0] == "Run one foundation lesson."


def main() -> None:
    test_practice_plan_has_steps()
    print("test_pfpython_practice.py passed.")


if __name__ == "__main__":
    main()
