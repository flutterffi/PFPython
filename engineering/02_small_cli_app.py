"""Engineering lesson 02: a tiny command-line app."""

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="Create a small study task message.")
    parser.add_argument("--task", default="practice functions", help="The study task to show.")
    parser.add_argument("--priority", default="medium", help="The task priority.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Task: {args.task}")
    print(f"Priority: {args.priority}")
    print("Next action: finish the task, then refactor the script into smaller functions.")


if __name__ == "__main__":
    main()
