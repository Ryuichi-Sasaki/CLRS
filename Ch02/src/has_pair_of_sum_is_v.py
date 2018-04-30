"""
    n個の整数の集合Sの中から、a+b=v(a,b ∈ S)となるような
    組み合わせが存在するかどうかを調べる。
"""


from binary_search import binary_search
from merge_sort import merge_sort


def has_pair_of_sum_is_v(A, v):
    B = list(A)
    merge_sort(B)
    for i in range(0, len(B) - 1):
        if binary_search(B[i + 1:], v - B[i]) is not None:
            return True
    else:
        return False