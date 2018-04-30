import unittest
import sys
sys.path.append("../src/")
from has_pair_of_sum_is_v import has_pair_of_sum_is_v


class TestBinarySearch(unittest.TestCase):
    def test_has_pair_of_sum_is_v_not_exist(self):
        A = {8, 3, 9, 1, 7, 4}
        b = has_pair_of_sum_is_v(A, 14)
        self.assertFalse(b)

    def test_has_pair_of_sum_is_v_exist(self):
        A = {8, 3, 9, 1, 7, 4}
        b = has_pair_of_sum_is_v(A, 15)
        self.assertTrue(b)


if __name__ == "__main__":
    unittest.main()
