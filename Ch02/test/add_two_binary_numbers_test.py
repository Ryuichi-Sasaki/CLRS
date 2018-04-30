import unittest
import sys
sys.path.append("../src/")
from add_two_binary_numbers import add_two_binary_numbers


class TestAddTwoBinaryNumbers(unittest.TestCase):
    def test_add_two_binary_numbers_without_carry(self):
        A = [0, 1, 1, 0, 1]
        B = [0, 0, 0, 1, 0]
        C = [0, 0, 0, 0, 0, 0]
        add_two_binary_numbers(A, B, C)
        self.assertEqual(C, [0, 0, 1, 1, 1, 1])

    def test_add_two_binary_numbers_with_carry(self):
        A = [0, 1, 1, 0, 1]
        B = [1, 0, 1, 0, 1]
        C = [0, 0, 0, 0, 0, 0]
        add_two_binary_numbers(A, B, C)
        self.assertEqual(C, [1, 0, 0, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()