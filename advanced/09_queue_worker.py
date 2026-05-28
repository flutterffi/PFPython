"""Advanced lesson 09: a queue-based worker pattern."""

from queue import Queue
from threading import Thread


def worker(queue: Queue, output: list[str]) -> None:
    while True:
        item = queue.get()
        if item is None:
            queue.task_done()
            return
        output.append(f"processed:{item}")
        queue.task_done()


def main() -> None:
    queue: Queue = Queue()
    output: list[str] = []
    thread = Thread(target=worker, args=(queue, output))
    thread.start()

    for item in ["loops", "queues", "retry"]:
        queue.put(item)
    queue.put(None)
    queue.join()
    thread.join()

    print(output)


if __name__ == "__main__":
    main()
