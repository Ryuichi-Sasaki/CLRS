import unittest
import sys
sys.path.append("../src/")
from insertion_sort_recur import insertion_sort


class TestInsertionSortRecur(unittest.TestCase):
    def test_insertion_sort_already_sorted(self):
        A = [1, 2, 3, 4, 5, 6]
        insertion_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])

    def test_insertion_sort(self):
        A = [5, 2, 4, 6, 1, 3]
        insertion_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
