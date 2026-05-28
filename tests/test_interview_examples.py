"""Tests for interview practice examples."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_two_sum_example() -> None:
    module = load_module(PROJECT_ROOT / "interview" / "01_two_sum_dict.py", "two_sum_module")
    assert module.two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_palindrome_example() -> None:
    module = load_module(PROJECT_ROOT / "interview" / "02_palindrome_check.py", "palindrome_module")
    assert module.is_palindrome("A man, a plan, a canal: Panama") is True
    assert module.is_palindrome("python") is False


def test_word_frequency_example() -> None:
    module = load_module(PROJECT_ROOT / "interview" / "03_word_frequency.py", "frequency_module")
    report = module.frequency_report("python practice python")
    assert report[0] == ("python", 2)


def main() -> None:
    test_two_sum_example()
    test_palindrome_example()
    test_word_frequency_example()
    print("test_interview_examples.py passed.")


if __name__ == "__main__":
    main()
