"""Module lesson 03: command-line arguments with argparse."""

from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.practice import build_practice_plan


def parse_args() -> tuple[str, int]:
    parser = ArgumentParser(description="Simple CLI argument practice.")
    parser.add_argument("--name", default="Learner", help="The learner name to greet.")
    parser.add_argument("--count", type=int, default=2, help="How many practice steps to show.")
    args = parser.parse_args()
    return args.name, args.count


def main() -> None:
    name, count = parse_args()
    print(f"Hello, {name}.")
    print("Your short practice plan:")
    for item in build_practice_plan()[:count]:
        print(f"- {item}")


if __name__ == "__main__":
    main()
