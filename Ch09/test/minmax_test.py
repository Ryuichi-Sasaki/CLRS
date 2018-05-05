import unittest
import sys
sys.path.append("../src/")
from minmax import minmax
from minmax import minmax_fast
from random import randint


class TestMinMax(unittest.TestCase):
    def test_minmax(self):
        A = {randint(-100, 100) for _ in range(30)}
        expected = (min(A), max(A))
        actual = minmax(A)
        self.assertEqual(expected, actual)

    def test_minmax_fast(self):
        A = {randint(-100, 100) for _ in range(30)}
        expected = (min(A), max(A))
        actual = minmax_fast(A)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
