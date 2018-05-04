import unittest
import sys
sys.path.append("../src/")
from quick_sort import quick_sort
from random import randint


class TestQuickSort(unittest.TestCase):
    def test_quick_sort_already_sorted(self):
        A = sorted([randint(-10, 10) for _ in range(30)])
        B = A.copy()
        quick_sort(B)
        self.assertEqual(A, B)

    def test_quick_sort(self):
        A = [randint(-10, 10) for _ in range(30)]
        B = A.copy()
        A.sort()
        quick_sort(B)
        self.assertEqual(A, B)


if __name__ == "__main__":
    unittest.main()
