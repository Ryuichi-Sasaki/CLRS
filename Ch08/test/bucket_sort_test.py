import unittest
import sys
sys.path.append("../src/")
from bucket_sort import bucket_sort
from random import random


class TestBucketSort(unittest.TestCase):
    def test_bucket_sort_already_sorted(self):
        A = sorted([random() for _ in range(30)])
        B = A.copy()
        B = bucket_sort(B)
        self.assertEqual(A, B)

    def test_bucket_sort(self):
        A = [random() for _ in range(30)]
        B = A.copy()
        A.sort()
        B = bucket_sort(B)
        self.assertEqual(A, B)


if __name__ == "__main__":
    unittest.main()
