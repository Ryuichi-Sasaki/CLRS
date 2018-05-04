"""
    バケツソート

    全要素を対応するバケツに入れ、
    各バケツ内を挿入ソートにより整列し、順に取り出す。

    入力が一様分布から抽出される場合に、平均実行時間O(n)
    この実装では安定ソート。
"""

import sys
sys.path.append("../../Ch02/src/")
from insertion_sort import insertion_sort
from math import floor


def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[floor(n * A[i])].append(A[i])
    for i in range(n):
        insertion_sort(B[i])
    return [e for sub in B for e in sub]