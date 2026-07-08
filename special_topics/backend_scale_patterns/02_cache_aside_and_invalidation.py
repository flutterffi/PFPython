"""Practice cache-aside reads and invalidation tradeoffs."""

from dataclasses import dataclass


@dataclass
class CacheEntry:
    key: str
    value: dict[str, object]
    stale: bool = False


class FakeCache:
    def __init__(self) -> None:
        self.entries: dict[str, CacheEntry] = {}

    def get(self, key: str) -> CacheEntry | None:
        return self.entries.get(key)

    def set(self, key: str, value: dict[str, object]) -> None:
        self.entries[key] = CacheEntry(key=key, value=value, stale=False)

    def invalidate(self, key: str) -> None:
        if key in self.entries:
            self.entries[key].stale = True


class FakeRepository:
    def load_topic(self, topic: str) -> dict[str, object]:
        return {"topic": topic, "version": 2, "source": "repository"}


def fetch_topic(topic: str, cache: FakeCache, repository: FakeRepository) -> dict[str, object]:
    cache_key = f"topic:{topic}"
    entry = cache.get(cache_key)

    if entry and not entry.stale:
        return {"mode": "cache-hit", "payload": entry.value}

    payload = repository.load_topic(topic)
    cache.set(cache_key, payload)
    return {"mode": "cache-miss", "payload": payload}


def main() -> None:
    cache = FakeCache()
    repository = FakeRepository()

    first = fetch_topic("fastapi", cache, repository)
    second = fetch_topic("fastapi", cache, repository)
    cache.invalidate("topic:fastapi")
    third = fetch_topic("fastapi", cache, repository)

    print("Cache-aside flow")
    print("=" * 16)
    print(first)
    print(second)
    print(third)
    print("\nHigh-level questions:")
    print("- who owns invalidation after writes")
    print("- what if stale data is acceptable for 30 seconds")
    print("- what cache keys explode under high-cardinality inputs")


if __name__ == "__main__":
    main()
