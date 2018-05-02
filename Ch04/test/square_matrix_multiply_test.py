import unittest
import sys
sys.path.append("../src/")
from square_matrix_multiply import square_matrix_multiply
from square_matrix_multiply import square_matrix_multiply_recur
from square_matrix_multiply import square_matrix_multiply_strassen
from random import randint


class TestSquareMatrixMultiply(unittest.TestCase):
    def test_square_matrix_multiply_recur(self):
        """ 分割統治法の結果が定義通りの計算の結果と一致することを確認する。  
        """
        # nは2のベキである必要がある
        n = 2 ** randint(1, 4)
        A = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
        B = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
        result1 = square_matrix_multiply(A, B)
        result2 = square_matrix_multiply_recur(A, B)
        self.assertEqual(result1, result2)

    def test_square_matrix_multiply_strassen(self):
        """ strassenのアルゴリズムの結果が定義通りの計算の結果と一致することを確認する。
        """
        # nは2のベキである必要がある
        n = 2 ** randint(1, 4)
        A = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
        B = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
        result1 = square_matrix_multiply(A, B)
        result2 = square_matrix_multiply_strassen(A, B)
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
