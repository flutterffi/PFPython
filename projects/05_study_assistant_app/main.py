"""Project 05: combine config, logging, and service helpers."""

from argparse import ArgumentParser
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from config import load_config
from logger import build_logger
from service import build_session, save_session


def parse_args():
    parser = ArgumentParser(description="A small study assistant app.")
    parser.add_argument("--topic", default="python", help="Topic to study.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config()
    logger = build_logger()

    session = build_session(
        topic=args.topic,
        minutes=int(config["default_minutes"]),
        mode=str(config["mode"]),
    )
    save_session(session)
    logger.info(session["message"])
    print(session)


if __name__ == "__main__":
    main()
