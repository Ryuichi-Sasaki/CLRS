"""
    二分探索

    ＜最悪実行時間に関する漸化式＞
      T(n) = | Θ(1)        if n = 1
             | T(n/2) + c  if n > 1
    
    ループの度に検査範囲が半減するので、Θ(lgn)となる。
"""


def binary_search(A, v):
    left = 0
    right = len(A) - 1
    while left <= right:
        i = (left + right) // 2
        if v < A[i]:
            right = i - 1
        elif A[i] < v:
            left = i + 1
        else:
            return i
    else:
        return None