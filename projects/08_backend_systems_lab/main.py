"""Project 08: high-level backend systems lab."""

from argparse import ArgumentParser
from pathlib import Path
import sys
from uuid import uuid4

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import RequestContext
from service import SystemsLabService


def parse_args():
    parser = ArgumentParser(description="A backend systems training lab.")
    parser.add_argument("--topic", default="observability", help="Topic to request.")
    parser.add_argument("--forbid", action="store_true", help="Simulate missing scope.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    service = SystemsLabService()
    scopes = {"read:topics", "read:metrics"}
    if args.forbid:
        scopes = {"read:logs"}

    context = RequestContext(
        request_id=f"req-{uuid4().hex[:8]}",
        subject="advanced-learner",
        topic=args.topic,
        scopes=scopes,
        idempotency_key=f"idem-{args.topic}",
    )
    print(service.handle_request(context))


if __name__ == "__main__":
    main()
