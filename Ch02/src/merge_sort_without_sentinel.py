"""
    マージソート（番兵なし）
"""


def copy(dest, k, src, i):
    for x in src[i:]:
        dest[k] = x
        k += 1


def merge(A, p, q, r):
    """ ソート済みの二区間、A[p..q] と A[q+1..r]をマージする  
        p < q < r  
        Θ(n)
    """
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    for k in range(p, r + 1):
        if i == len(L):
            copy(A, k, R, j)
            break
        elif j == len(R):
            copy(A, k, L, i)
            break
        elif L[i] <= R[j]:
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