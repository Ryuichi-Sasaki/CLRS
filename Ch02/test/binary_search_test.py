import unittest
import sys
sys.path.append("../src/")
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_not_found(self):
        A = [1, 3, 4, 7, 8, 9]
        i = binary_search(A, 5)
        self.assertEqual(i, None)

    def test_binary_search_found(self):
        A = [1, 3, 4, 7, 8, 9]
        i = binary_search(A, 8)
        self.assertEqual(i, 4)


if __name__ == "__main__":
    unittest.main()
