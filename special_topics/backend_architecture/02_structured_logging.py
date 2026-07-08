"""Practice structured logging ideas in a backend-style flow."""

import json
import logging
from dataclasses import dataclass
from datetime import datetime, UTC


class JsonFormatter(logging.Formatter):
    """Render logs as JSON-like text for easy machine reading."""

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "time": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
        }

        request_id = getattr(record, "request_id", None)
        endpoint = getattr(record, "endpoint", None)
        if request_id:
            payload["request_id"] = request_id
        if endpoint:
            payload["endpoint"] = endpoint
        return json.dumps(payload, ensure_ascii=True)


def build_logger() -> logging.Logger:
    logger = logging.getLogger("pfpython.backend")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    return logger


@dataclass
class RequestContext:
    request_id: str
    endpoint: str


def handle_request(logger: logging.Logger, context: RequestContext) -> dict[str, str]:
    logger.info(
        "request started",
        extra={"request_id": context.request_id, "endpoint": context.endpoint},
    )

    result = {"status": "ok", "endpoint": context.endpoint}

    logger.info(
        "request completed",
        extra={"request_id": context.request_id, "endpoint": context.endpoint},
    )
    return result


def main() -> None:
    logger = build_logger()
    context = RequestContext(request_id="req-1001", endpoint="/lessons")
    result = handle_request(logger=logger, context=context)

    print("\nReturned response:")
    print(result)
    print("\nPractice ideas:")
    print("- add user_id or duration fields")
    print("- log validation failures")
    print("- write the same pattern for database calls")


if __name__ == "__main__":
    main()
