"""Project 09: event-driven workflow lab."""

from argparse import ArgumentParser
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from service import WorkflowLabService


def parse_args():
    parser = ArgumentParser(description="An event-driven workflow training lab.")
    parser.add_argument("--topic", default="payments", help="Topic to orchestrate.")
    parser.add_argument(
        "--fail-step",
        default=None,
        choices=["publish"],
        help="Simulate a failing workflow step.",
    )
    parser.add_argument(
        "--duplicate-publish",
        action="store_true",
        help="Simulate duplicated event publication.",
    )
    parser.add_argument(
        "--publish-fail-times",
        type=int,
        default=0,
        help="Simulate transient broker publish failures before success.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    service = WorkflowLabService()
    print(
        service.run_workflow(
            topic=args.topic,
            fail_step=args.fail_step,
            duplicate_publish=args.duplicate_publish,
            publish_fail_times=args.publish_fail_times,
        )
    )


if __name__ == "__main__":
    main()
