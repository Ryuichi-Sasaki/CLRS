"""
    クイックソート

    ＜ループ不変式＞
      partitionのfor文の各繰り返しの直前では、
      任意の配列添字kに対して以下の命題が成立する。
        1. l ≦ k ≦ i ならば、A[k] ≦ pivot である
        2. i + 1 ≦ k ≦ j - 1 ならば、A[k] > pivot である
        3. k = r ならば、A[k] = pivot である

    [期待実行時間]
      Θ(nlgn)
    
    [最悪実行時間（既ソートの場合）]
      Θ(n^2)
"""


def quick_sort(A, l = 0, r = None):
    r = len(A) - 1 if r is None else r

    if l < r:
        p = partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)


def partition(A, l, r):
    if all([x == A[l] for x in A[l+1:r+1]]):
        return (l + r) // 2

    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1
