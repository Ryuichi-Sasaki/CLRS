import unittest
import sys
sys.path.append("../src/")
from counting_sort import counting_sort
from random import randint


class TestCountingSort(unittest.TestCase):
    def test_counting_sort_already_sorted(self):
        A = sorted([randint(0, 100) for _ in range(30)])
        B = A.copy()
        C = counting_sort(B)
        self.assertEqual(A, C)

    def test_counting_sort(self):
        A = [randint(0, 100) for _ in range(30)]
        B = A.copy()
        A.sort()
        C = counting_sort(B)
        self.assertEqual(A, C)


if __name__ == "__main__":
    unittest.main()
