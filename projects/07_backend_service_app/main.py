"""Project 07: a backend-style practice app with logging and service layers."""

from argparse import ArgumentParser
from pathlib import Path
import sys
from uuid import uuid4

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from config import load_settings
from logger import build_logger
from repository import LessonRepository
from service import TopicService


def parse_args():
    parser = ArgumentParser(description="A backend-style lesson service app.")
    parser.add_argument("--topic", default=None, help="Topic to request.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    settings = load_settings()
    logger = build_logger()
    service = TopicService(
        repository=LessonRepository(),
        max_results=int(settings["max_results"]),
    )

    topic = args.topic or str(settings["default_topic"])
    request_id = f"req-{uuid4().hex[:8]}"

    logger.info(
        "topic request received",
        extra={"request_id": request_id, "topic": topic},
    )
    response = service.get_topic_response(topic).to_dict()
    logger.info(
        "topic request completed",
        extra={"request_id": request_id, "topic": topic},
    )

    print(response)


if __name__ == "__main__":
    main()
