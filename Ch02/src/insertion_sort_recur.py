"""
    挿入ソート（再帰版）

    ＜最悪実行時間に関する漸化式＞
      T(n) = | Θ(1)          if n = 1
             | T(n-1) + Θ(n) if n > 1
"""


def insert(A, j):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key


def isort(A, i):
    if i > 0:
        isort(A, i - 1)
        insert(A, i)


def insertion_sort(A):
    isort(A, len(A) - 1)