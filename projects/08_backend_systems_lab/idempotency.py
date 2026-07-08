"""Idempotency control for the backend systems lab."""


class IdempotencyStore:
    def __init__(self) -> None:
        self._responses: dict[str, dict[str, object]] = {}

    def get(self, key: str) -> dict[str, object] | None:
        return self._responses.get(key)

    def remember(self, key: str, response: dict[str, object]) -> None:
        self._responses[key] = response


def main() -> None:
    store = IdempotencyStore()
    store.remember("idem-1", {"status": "ok"})
    print("Idempotency lab demo")
    print("=" * 20)
    print(store.get("idem-1"))


if __name__ == "__main__":
    main()
