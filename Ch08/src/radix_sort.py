"""
    基数ソート

    比較によらないソート。
    ソート対象の桁を利用してソートを行う。
    上位桁優先とするため、下位桁から上位桁の順にソートする。
    全要素の桁数が一致している必要がある。

    n個のd桁の数をソートする場合、
    サブルーチンとして用いる安定ソートの実行時間がΘ(n + k)のとき、
    基数ソートの実行時間はΘ(d(n + k))。
    安定ソート。
"""


def counting_sort(A, proc):
    B = A.copy()
    k = max([proc(n) for n in A])
    C = [0] * (k + 1)
    # 分布を数える
    for j in range(len(A)):
        C[proc(A[j])] += 1
    # 書き込む場所を求める
    for i in range(k):
        C[i + 1] += C[i]
    # 書き込む
    for j in range(len(A) - 1, -1, -1):
        B[C[proc(A[j])] - 1] = A[j]
        C[proc(A[j])] -= 1
    return B


def radix_sort(A, d):
    for i in range(d - 1, -1, -1):
        # Aの第i桁の抽出手続き
        extracor = lambda n: int(str(n)[i])
        # 第i桁でソートする
        A = counting_sort(A, extracor)
    return A