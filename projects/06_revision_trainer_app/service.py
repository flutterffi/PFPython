"""Project 06 service helpers."""


def build_session(topic: str, attempt: int, worker_name: str) -> dict[str, object]:
    return {
        "topic": topic,
        "attempt": attempt,
        "worker": worker_name,
        "message": f"Review {topic} with {worker_name} on attempt {attempt}.",
    }


def run_revision(topic: str, max_attempts: int, worker_name: str) -> dict[str, object]:
    for attempt in range(1, max_attempts + 1):
        if attempt == max_attempts:
            return build_session(topic, attempt, worker_name)
    raise RuntimeError("No attempts were available.")


def main() -> None:
    print(run_revision("queues", 3, "trainer-worker"))


if __name__ == "__main__":
    main()
