"""Engineering lesson 08: the built-in unittest module."""

from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.math_utils import fibonacci, is_prime


class MathUtilsTests(unittest.TestCase):
    def test_fibonacci_sequence(self) -> None:
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_prime_checks(self) -> None:
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(18))


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(MathUtilsTests)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
