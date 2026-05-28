"""Project 06 queue worker helpers."""

from queue import Queue
from threading import Thread


def run_worker(topic: str, worker_name: str) -> list[str]:
    queue: Queue = Queue()
    output: list[str] = []

    def consume() -> None:
        while True:
            item = queue.get()
            if item is None:
                queue.task_done()
                return
            output.append(f"{worker_name}:{item}")
            queue.task_done()

    thread = Thread(target=consume)
    thread.start()
    queue.put(topic)
    queue.put(None)
    queue.join()
    thread.join()
    return output


def main() -> None:
    print(run_worker("retry", "trainer-worker"))


if __name__ == "__main__":
    main()
