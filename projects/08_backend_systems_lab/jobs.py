"""Background job simulation for the backend systems lab."""

from dataclasses import dataclass


@dataclass
class JobRecord:
    name: str
    state: str


class JobQueue:
    def __init__(self) -> None:
        self.scheduled: list[JobRecord] = []

    def schedule(self, name: str) -> JobRecord:
        record = JobRecord(name=name, state="scheduled")
        self.scheduled.append(record)
        return record


def main() -> None:
    queue = JobQueue()
    print("Jobs lab demo")
    print("=" * 13)
    print(queue.schedule("refresh-topic-cache"))


if __name__ == "__main__":
    main()
