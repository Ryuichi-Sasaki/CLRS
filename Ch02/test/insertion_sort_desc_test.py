import unittest
import sys
sys.path.append("../src/")
from insertion_sort_desc import insertion_sort_desc


class TestInsertionSortDesc(unittest.TestCase):
    def test_insertion_sort_desc_already_sorted(self):
        A = [6, 5, 4, 3, 2, 1]
        insertion_sort_desc(A)
        self.assertEqual(A, [6, 5, 4, 3, 2, 1])

    def test_insertion_sort_desc(self):
        A = [5, 2, 4, 6, 1, 3]
        insertion_sort_desc(A)
        self.assertEqual(A, [6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
