"""Project 06: combine config, queue work, retry thinking, and persistence."""

from argparse import ArgumentParser
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from config import load_config
from repository import load_sessions, save_sessions
from service import run_revision
from worker import run_worker


def parse_args():
    parser = ArgumentParser(description="A revision trainer app.")
    parser.add_argument("--topic", default="python", help="Topic to revise.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config()
    session = run_revision(
        topic=args.topic,
        max_attempts=int(config["max_attempts"]),
        worker_name=str(config["worker_name"]),
    )
    worker_output = run_worker(args.topic, str(config["worker_name"]))

    sessions = load_sessions()
    sessions.append(session)
    save_sessions(sessions)

    print(session)
    print(worker_output)


if __name__ == "__main__":
    main()
