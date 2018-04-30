import unittest
import sys
sys.path.append("../src/")
from linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_not_found(self):
        A = [5, 2, 4, 6, 1, 3]
        i = linear_search(A, 7)
        self.assertEqual(i, None)

    def test_linear_search_found(self):
        A = [5, 2, 4, 6, 1, 3]
        i = linear_search(A, 1)
        self.assertEqual(i, 4)


if __name__ == "__main__":
    unittest.main()
