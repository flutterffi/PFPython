"""Engineering lesson 05: using unittest.mock for behavior checks."""

from unittest.mock import Mock


def send_reminder(notifier, topic: str) -> str:
    message = f"Remember to practice {topic}."
    notifier(message)
    return message


def main() -> None:
    notifier = Mock()
    message = send_reminder(notifier, "decorators")
    notifier.assert_called_once_with("Remember to practice decorators.")

    print(message)
    print(f"call count = {notifier.call_count}")


if __name__ == "__main__":
    main()
