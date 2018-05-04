"""
    クイックソート（乱択版）

    ピボットをランダムに選択することで、
    既ソートの入力に対しても良好な実行時間を達成する。

    [期待実行時間]
      Θ(nlgn)
"""


from random import randint
from quick_sort import partition


def randomized_quick_sort(A, l = 0, r = None):
    r = len(A) - 1 if r is None else r

    if l < r:
        p = randomized_partition(A, l, r)
        randomized_quick_sort(A, l, p - 1)
        randomized_quick_sort(A, p + 1, r)


def randomized_partition(A, l, r):
    i = randint(l, r)
    A[r], A[i] = A[i], A[r]

    return partition(A, l, r)
