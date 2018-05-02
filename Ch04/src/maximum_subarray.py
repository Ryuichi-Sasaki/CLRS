"""
    過去の株価チャートが終値の配列で与えられる。
    一度だけ買い、後日一度に全て売るとすると、
    利益が最大となる買いと売りはどこで、その差額はいくらか。

    ＜方法＞
      ・総当たり法
      ・分割統治法
      ・Kadaneのアルゴリズム

    [総当たり法]
      (買い,売り)の順序対を全て調べる。
      T(n) = Θ(n^2)

    [分割統治法]
      問題の見方を変える。
      終値の配列を前日からの変動の配列へ変換する。
      この変動配列における最大部分配列が、株を保有する期間となる。
      配列を左部分配列と右部分配列へ二分する。
      最大部分配列は、
       1.左部分配列に完全に含まれる
       2.右部分配列に完全に含まれる
       3.全体に含まれる（左右の境界を跨ぐ）
      のどれかである。

      T(n) = | Θ(1)            if n = 1
             | 2T(n/2) + Θ(n)  if n > 1

      これは、Θ(nlgn)である。
    
    [Kadaneのアルゴリズム]
      A[0..j+1]の最大部分配列は、次のどちらかである。
       1.A[0..j]の最大部分配列
       2.A[i..j+1]の最大部分配列（0 ≦ i ≦ j+1）
      T(n) = Θ(n)
"""


from random import randint


def maximum_diff_brute_force(A):
    """ 総当たり法 Θ(n^2)
    """
    left = 0
    right = 0
    max_diff = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_diff:
                left = i
                right = j
                max_diff = A[j] - A[i]
    return (left, right, max_diff)


def maximum_diff_divide_and_conquer(A):
    """ 分割統治法 Θ(nlgn)
    """
    def maximum_crossing_subarray(D, low, mid, high):
        """ Θ(n)
        """
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += D[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        sum = 0
        for j in range(mid + 1, high + 1):
            sum += D[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
        return (max_left, max_right, left_sum + right_sum)

    def maximum_subarray(D, low, high):
        """ Θ(nlgn)
        """
        if high == low:
            return (low, high, D[low])
        else:
            mid = (low + high) // 2
            (l_low, l_high, l_sum) = maximum_subarray(D, low, mid)
            (r_low, r_high, r_sum) = maximum_subarray(D, mid + 1, high)
            (c_low, c_high, c_sum) = maximum_crossing_subarray(D, low, mid, high)
            maximum = max(l_sum, r_sum, c_sum)
            if maximum == l_sum:
                return (l_low, l_high, l_sum)
            elif maximum == r_sum:
                return (r_low, r_high, r_sum)
            else:
                return (c_low, c_high, c_sum)

    D = [next - prev for (prev, next) in zip(A, A[1:])]
    (low, high, max_diff) = maximum_subarray(D, 0, len(D) - 1)
    return (low, high + 1, max_diff)


def maximum_diff_dynamic_programming(A):
    """ Kadaneのアルゴリズム Θ(n)
    """
    def maximum_subarray(D):
        """ Θ(n)
        """
        prev_left, prev_right = 0, 0
        cur_left, cur_right = 0, 0
        prev_max_sum, cur_max_sum = D[0], D[0]
        for i in range(1, len(D)):
            cur_max_sum += D[i]
            cur_right += 1
            if D[i] > cur_max_sum:
                cur_max_sum = D[i]
                cur_left, cur_right = i, i
            if prev_max_sum < cur_max_sum:
                prev_max_sum = cur_max_sum
                prev_left, prev_right = cur_left, cur_right
        return (prev_left, prev_right, prev_max_sum)

    D = [next - prev for (prev, next) in zip(A, A[1:])]
    (low, high, max_diff) = maximum_subarray(D)
    return (low, high + 1, max_diff)
