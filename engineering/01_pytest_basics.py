"""Engineering lesson 01: test thinking without a test runner."""


def add_points(current: int, earned: int) -> int:
    return current + earned


def run_checks() -> None:
    assert add_points(2, 3) == 5
    assert add_points(0, 0) == 0
    assert add_points(-1, 1) == 0


def main() -> None:
    run_checks()
    print("All checks passed.")
    print("Later, move these assertions into real pytest test files.")


if __name__ == "__main__":
    main()
