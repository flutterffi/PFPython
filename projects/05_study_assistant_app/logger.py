"""Project 05 logging helpers."""

import logging


def build_logger() -> logging.Logger:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    return logging.getLogger("study_assistant")


def main() -> None:
    logger = build_logger()
    logger.info("Logger ready")


if __name__ == "__main__":
    main()
