import unittest
import sys
sys.path.append("../src/")
from maximum_subarray import maximum_diff_brute_force
from maximum_subarray import maximum_diff_divide_and_conquer
from maximum_subarray import maximum_diff_dynamic_programming
from random import randint


class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_diff_divide_and_conquer(self):
        """ 分割統治法の結果が総当たり法の結果と一致することを確認する。  
            最大部分配列は複数存在するかもしれないので、部分和だけ確認する。
        """
        A = [randint(0, 100) for _ in range(100)]
        (_, _, max_diff1) = maximum_diff_brute_force(A)
        (_, _, max_diff2) = maximum_diff_divide_and_conquer(A)
        self.assertEqual(max_diff1, max_diff2)

    def test_maximum_diff_dynamic_programming(self):
        """ kadaneのアルゴリズムの結果が総当たり法の結果と一致することを確認する。  
            最大部分配列は複数存在するかもしれないが、どちらも最も左に存在するものの情報を  
            返すので、結果が全て一致するか確認できる。
        """
        A = [randint(0, 100) for _ in range(100)]
        result1 = maximum_diff_brute_force(A)
        result2 = maximum_diff_dynamic_programming(A)
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
