import unittest
import sys
sys.path.append("../src/")
from merge_sort_without_sentinel import merge_sort


class TestMergeSortWithoutSentinel(unittest.TestCase):
    def test_merge_sort_already_sorted(self):
        A = [1, 2, 3, 4, 5, 6]
        merge_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])

    def test_merge_sort(self):
        A = [5, 2, 4, 6, 1, 3]
        merge_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
