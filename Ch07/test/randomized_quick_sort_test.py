import unittest
import sys
sys.path.append("../src/")
from randomized_quick_sort import randomized_quick_sort
from random import randint


class TestRandomizedQuickSort(unittest.TestCase):
    def test_randomized_quick_sort_already_sorted(self):
        A = sorted([randint(-10, 10) for _ in range(30)])
        B = A.copy()
        randomized_quick_sort(B)
        self.assertEqual(A, B)

    def test_randomized_quick_sort(self):
        A = [randint(-10, 10) for _ in range(30)]
        B = A.copy()
        A.sort()
        randomized_quick_sort(B)
        self.assertEqual(A, B)


if __name__ == "__main__":
    unittest.main()
