"""
    計数ソート（分布数えソート）

    比較によらないソート。
    入力配列中の要素xについてxより小さい要素の数を数えて、
    出力配列へxを書き込む位置の決定に利用する。
    入力配列の要素は非負整数である必要がある。

    安定で、Θ(n + k)。
"""


def counting_sort(A):
    def csort(k):
        C = [0] * (k + 1)

        # 分布を数える
        for j in range(len(A)):
            C[A[j]] += 1
        
        # 書き込む場所を求める
        for i in range(k):
            C[i+1] += C[i]
        
        # 書き込む
        for j in range(len(A) - 1, -1, -1):
            B[C[A[j]] - 1] = A[j]
            C[A[j]] -= 1

    B = [0] * len(A)
    csort(max(A))
    return B