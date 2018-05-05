import unittest
import sys
sys.path.append("../src/")
from randomized_select import randomized_select
from randomized_select import randomized_select_iter
from random import randint


class TestRandomizedSelect(unittest.TestCase):
    def test_randomized_select(self):
        n = randint(1, 30)
        i = randint(1, n)
        A = [randint(-100, 100) for _ in range(n)]
        B = A.copy()
        for _ in range(i - 1):
            A.remove(min(A))
        expected = min(A)
        actual = randomized_select(B, 0, len(B) - 1, i)
        self.assertEqual(expected, actual)

    def test_randomized_select_iter(self):
        n = randint(1, 30)
        i = randint(1, n)
        A = [randint(-100, 100) for _ in range(n)]
        B = A.copy()
        for _ in range(i - 1):
            A.remove(min(A))
        expected = min(A)
        actual = randomized_select_iter(B, i)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
