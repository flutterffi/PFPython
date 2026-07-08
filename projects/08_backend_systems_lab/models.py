"""Shared models for the backend systems lab."""

from dataclasses import asdict, dataclass


@dataclass
class RequestContext:
    request_id: str
    subject: str
    topic: str
    scopes: set[str]
    idempotency_key: str


@dataclass
class TopicSummary:
    topic: str
    source: str
    message: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def main() -> None:
    model = TopicSummary(topic="observability", source="cache", message="ready")
    print("Models lab demo")
    print("=" * 15)
    print(model.to_dict())


if __name__ == "__main__":
    main()
