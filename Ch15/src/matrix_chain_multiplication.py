"""
    連鎖行列積問題

    (p,q)型行列と(q,r)型行列の積は(p,r)型行列になる。  
    この計算にはpqr回の乗算を必要とする。  

    複数の行列の積を計算することを考える。  
    行列の積は結合的なので、どこから計算しても結果は同じ。  
    どの隣り合った行列の積から計算するかで必要となる乗算の回数が変わる。

    最も効率良く計算するにはどこから計算すればよいか。
"""


def matrix_chain_order(p):
    """ θ(n^3)  
        連鎖行列積を計算する際の最適な分割点を求めて返す。
    """
    n = len(p) - 1
    m, s = dict(), dict()
    pass
    for i in range(1, n + 1):
        m[(i,i)] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[(i,j)] = float("inf")
            for k in range(i, j):
                q = m[(i,k)] + m[(k+1,j)] + p[i-1]*p[k]*p[j]
                if q < m[(i,j)]:
                    m[(i,j)] = q
                    s[(i,j)] = k
    return (m, s)


def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[(i,j)])
        print_optimal_parens(s, s[(i,j)] + 1, j)
        print(")", end="")


def matrix_chain_maltiply(As, s, i, j):
    """ 最適な順序で連鎖行列積の計算を行う。
    """
    def matrix_multiply(A, B):
        a_row = len(A)
        a_col = len(A[0])
        b_col = len(B[0])
        C = [[0] * b_col for _ in range(a_row)]
        for i in range(a_row):
            for j in range(b_col):
                for k in range(a_col):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    if i == j:
        return As[i - 1]
    left = matrix_chain_maltiply(As, s, i, s[(i,j)])
    right = matrix_chain_maltiply(As, s, s[(i,j)] + 1, j)
    return matrix_multiply(left, right)
