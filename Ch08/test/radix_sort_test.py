import unittest
import sys
sys.path.append("../src/")
from radix_sort import radix_sort
from random import randint


class TestRadixSort(unittest.TestCase):
    def test_radix_sort_already_sorted(self):
        d = 10
        A = sorted([randint(10**(d-1), 10**d-1) for _ in range(30)])
        B = A.copy()
        B = radix_sort(B, d)
        self.assertEqual(A, B)

    def test_radix_sort(self):
        d = 10
        A = [randint(10**(d-1), 10**d-1) for _ in range(30)]
        B = A.copy()
        A.sort()
        B = radix_sort(B, d)
        self.assertEqual(A, B)


if __name__ == "__main__":
    unittest.main()
