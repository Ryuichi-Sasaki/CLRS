"""
    線形期待時間選択アルゴリズム

    入力配列中のi番目に小さい要素を見つける。
    期待実行時間O(n)。
"""


import sys
sys.path.append("../../Ch07/src")
from randomized_quick_sort import randomized_partition


def randomized_select(A, l, r, i):
    if l == r:
        return A[l]
    q = randomized_partition(A, l, r)
    k = q - l + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, l, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


def randomized_select_iter(A, i):
    l, r = 0, len(A) - 1
    while l < r:
        q = randomized_partition(A, l, r)
        k = q - l + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q - 1
        else:
            l = q + 1
            i -= k
    return A[l]
