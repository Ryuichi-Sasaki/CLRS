import unittest
import sys
sys.path.append("../src/")
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_already_sorted(self):
        A = [1, 2, 3, 4, 5, 6]
        selection_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])

    def test_selection_sort(self):
        A = [5, 2, 4, 6, 1, 3]
        selection_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
