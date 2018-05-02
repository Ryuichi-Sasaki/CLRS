"""
    n×n行列A,Bの積を計算する

    ＜方法＞
      ・定義通り
      ・分割統治法
      ・strassenの方法
    
    [定義通り]
      c_ij = Σ(k=1 to n)a_ik*b_kj

      Θ(n^3)

    [分割統治法]
      A,Bをn/2*n/2型の4つの行列に分解して計算する。

      T(n) = | Θ(1)              if n = 1
             | 8T(n/2) + Θ(n^2)  if n > 1

      マスター法よりΘ(n^3)

    [strassenの方法]
      詳細はググって。

      T(n) = | Θ(1)              if n = 1
             | 7T(n/2) + Θ(n^2)  if n > 1

      マスター法よりΘ(n^lg7)
"""


def make_square_matrix(size):
    """ Θ(size^2)
    """
    return [[0] * size for _ in range(size)]


def copy(A, i_start, j_start, size):
    """ Θ(size^2)
    """
    B = make_square_matrix(size)
    for i in range(size):
        for j in range(size):
            B[i][j] = A[i_start + i][j_start + j]
    return B


def split(A):
    """ Θ(n^2)
    """
    size = len(A) // 2
    A11 = copy(A, 0, 0, size)
    A12 = copy(A, 0, size, size)
    A21 = copy(A, size, 0, size)
    A22 = copy(A, size, size, size)
    return (A11, A12, A21, A22)


def matrix_sum(A, B):
    """ Θ(n^2)
    """
    n = len(A)
    C = make_square_matrix(n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def matrix_diff(A, B):
    """ Θ(n^2)
    """
    n = len(A)
    C = make_square_matrix(n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def combine(ul, ur, ll, lr):
    """ Θ(??)
    """
    u = list(map(lambda x, y: x + y, ul, ur))
    l = list(map(lambda x, y: x + y, ll, lr))
    return u + l


def square_matrix_multiply(A, B):
    """ 定義通りの計算 Θ(n^3)
    """
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def square_matrix_multiply_recur(A, B):
    """ 分割統治法 Θ(n^3)
    """
    if len(A) == 1:
        C = make_square_matrix(1)
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11, A12, A21, A22 = split(A)
        B11, B12, B21, B22 = split(B)
        C11 = matrix_sum(square_matrix_multiply_recur(A11, B11)
                        ,square_matrix_multiply_recur(A12, B21))
        C12 = matrix_sum(square_matrix_multiply_recur(A11, B12)
                        ,square_matrix_multiply_recur(A12, B22))
        C21 = matrix_sum(square_matrix_multiply_recur(A21, B11)
                        ,square_matrix_multiply_recur(A22, B21))
        C22 = matrix_sum(square_matrix_multiply_recur(A21, B12)
                        ,square_matrix_multiply_recur(A22, B22))
        return combine(C11, C12, C21, C22)


def square_matrix_multiply_strassen(A, B):
    """ strassenのアルゴリズム Θ(n^lg7)
    """
    if len(A) == 1:
        C = make_square_matrix(1)
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11, A12, A21, A22 = split(A)
        B11, B12, B21, B22 = split(B)
        S1 = matrix_diff(B12, B22)
        S2 = matrix_sum(A11, A12)
        S3 = matrix_sum(A21, A22)
        S4 = matrix_diff(B21, B11)
        S5 = matrix_sum(A11, A22)
        S6 = matrix_sum(B11, B22)
        S7 = matrix_diff(A12, A22)
        S8 = matrix_sum(B21, B22)
        S9 = matrix_diff(A11, A21)
        S10 = matrix_sum(B11, B12)
        P1 = square_matrix_multiply_strassen(A11, S1)
        P2 = square_matrix_multiply_strassen(S2, B22)
        P3 = square_matrix_multiply_strassen(S3, B11)
        P4 = square_matrix_multiply_strassen(A22, S4)
        P5 = square_matrix_multiply_strassen(S5, S6)
        P6 = square_matrix_multiply_strassen(S7, S8)
        P7 = square_matrix_multiply_strassen(S9, S10)
        C11 = matrix_sum(matrix_diff(matrix_sum(P5, P4), P2), P6)
        C12 = matrix_sum(P1, P2)
        C21 = matrix_sum(P3, P4)
        C22 = matrix_diff(matrix_diff(matrix_sum(P5, P1), P3), P7)
        return combine(C11, C12, C21, C22)
