"""Tests for pfpython.math_utils."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.math_utils import fibonacci, is_prime


def test_fibonacci_values() -> None:
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_prime_values() -> None:
    assert is_prime(19) is True
    assert is_prime(21) is False


def main() -> None:
    test_fibonacci_values()
    test_prime_values()
    print("test_math_utils.py passed.")


if __name__ == "__main__":
    main()
