"""Engineering lesson 06: structured logging basics."""

import logging


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    configure_logging()
    logger = logging.getLogger("pfpython.practice")
    logger.info("Starting practice session")
    logger.warning("This is a reminder to keep examples small")
    logger.info("Finished practice session")


if __name__ == "__main__":
    main()
