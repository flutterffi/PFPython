"""Practice background job retries and dead-letter decisions."""

from dataclasses import dataclass


@dataclass
class Job:
    name: str
    attempts: int = 0


def process_job(job: Job, max_attempts: int) -> dict[str, object]:
    history: list[str] = []

    while job.attempts < max_attempts:
        job.attempts += 1
        history.append(f"attempt-{job.attempts}")
        if job.name != "poison-message":
            return {"status": "completed", "attempts": job.attempts, "history": history}

    return {"status": "dead-lettered", "attempts": job.attempts, "history": history}


def main() -> None:
    normal = process_job(Job(name="refresh-cache"), max_attempts=3)
    poison = process_job(Job(name="poison-message"), max_attempts=3)

    print("Background job flow")
    print("=" * 19)
    print(normal)
    print(poison)
    print("\nHigh-level questions:")
    print("- which failures deserve retry vs immediate dead-letter")
    print("- should backoff live in the worker or queue system")
    print("- what metadata is needed for replay")


if __name__ == "__main__":
    main()
