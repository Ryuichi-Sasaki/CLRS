"""
    マージソート

    ＜ループ不変式＞
      mergeの最後のfor文の繰り返しの開始時点では、
      部分列A[p..k-1]にはL[1..n1+1]とR[1..n2+1]が含む要素全体の中で
      小さい方からk-p個の要素がソートされた順序で置かれている。
      またL[i]とR[j]は配列LとRのまだAに書き戻されていない要素の中で
      最小の要素である。

    ＜最悪実行時間に関する漸化式＞
      T(n) = | Θ(1)            if n = 1
             | 2T(n/2) + Θ(n)  if n > 1
    
    cn + 2T(n/2) の形の再帰木を描けば、Θ(nlgn)であることがわかる。
"""


def merge(A, p, q, r):
    """ ソート済みの二区間、A[p..q] と A[q+1..r]をマージする  
        p < q < r  
        Θ(n)
    """
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def msort(A, p, r):
    if p < r:
        q = (p + r) // 2
        msort(A, p, q)
        msort(A, q + 1, r)
        merge(A, p, q, r)


def merge_sort(A):
    msort(A, 0, len(A) - 1)
