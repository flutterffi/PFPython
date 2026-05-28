"""Mark a practice file as complete in learner progress data."""

from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.progress import mark_file_complete


def parse_args():
    parser = ArgumentParser(description="Mark a practice file as complete.")
    parser.add_argument("--file", required=True, help="Repository-relative Python file path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    progress = mark_file_complete(args.file)
    print(f"Marked complete: {args.file}")
    print(f"Completed files: {len(progress['completed_files'])}")


if __name__ == "__main__":
    main()
