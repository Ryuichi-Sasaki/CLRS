"""
    最長共通部分列問題(Longest Common Subsequence problem)

    部分列：列の各要素を残すか残さないかしてできる列

    2つの列X、Yについて、最長である共通の部分列は何か？

    ＜素朴な方法＞
      2つの列それぞれについて全部分列を列挙し、  
      共通の部分列から最長であるものを探す。

    ＜再帰的トップダウン方式＞
      X[-1]とY[-1]が等しい場合：  
        LCSの最後尾はX[-1]となる。  
        X[:-1]とY[:-1]のLCSにX[-1]を連接したものが答え。

      X[-1]とY[-1]が異なる場合：  
        X[:-1]とYのLCSか、XとY[:-1]のLCSの長い方が答え。
    
    ＜動的計画法＞
      ＜トップダウン方式＞
        上の方法をメモ化するだけ。

      ＜ボトムアップ方式＞
        LCS長の表を作る。
"""


def naive_LCS(X, Y):
    """ O(2^n*2^m)
    """
    def subsequences(X):
        """ θ(2^n)
            入力列の全部分列を返す
        """
        if X == []:
            return [[]]
        prev = subsequences(X[1:])
        return prev + [[X[0]] + e for e in prev]

    x_subs = subsequences(X)
    y_subs = subsequences(Y)
    common_subs = [x for x in x_subs if x in y_subs]
    return max(common_subs, key=lambda sub: len(sub))


def bottom_up_LCS_length(X, Y):
    """ θ(mn) m:len(X), n:len(Y)  
        ボトムアップでLCS長の表を作成する。
    """
    m, n = len(X), len(Y)
    b = [[None] * n for _ in range(m)]
    c = [[None] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i][j] = "↖︎"
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = "↑"
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = "←"
    return (b, c)


def memoized_LCS_length(X, Y):
    """ O(mn) m:len(X), n:len(Y)  
        履歴管理でLCS長の表を作成する。
    """
    def memoized_LCS_length_aux(i, j):
        if c[i-1][j] == None:
            memoized_LCS_length_aux(i-1, j)
        if c[i][j-1] == None:
            memoized_LCS_length_aux(i, j-1)
        if X[i-1] == Y[j-1]:
            c[i][j] = c[i-1][j-1] + 1
            b[i-1][j-1] = "↖︎"
        elif c[i-1][j] > c[i][j-1]:
            c[i][j] = c[i-1][j]
            b[i-1][j-1] = "↑"
        else:
            c[i][j] = c[i][j-1]
            b[i-1][j-1] = "←"

    m, n = len(X), len(Y)
    b = [[None] * n for _ in range(m)]
    c = [[None] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    memoized_LCS_length_aux(m, n)
    return (b, c)


def print_LCS(b, X, i, j):
    """ O(i+j)  
        補助表によりLCSを再構成する。
    """
    if i < 0 or j < 0:
        return
    if b[i][j] == "↖︎":
        print_LCS(b, X, i-1, j-1)
        print(X[i], end="")
    elif b[i][j] == "↑":
        print_LCS(b, X, i-1, j)
    else:
        print_LCS(b, X, i, j-1)


def rebuild_LCS(c, X, Y):
    """ O(m+n) m:len(X), n:len(Y)  
        LCS長の表からLCSを再構成する。
    """
    def rebuild_LCS_aux(i, j):
        if i == 0 or j == 0:
            return
        if X[i-1] == Y[j-1]:
            rebuild_LCS_aux(i-1, j-1)
            print(X[i-1], end="")
        elif c[i-1][j] > c[i][j-1]:
            rebuild_LCS_aux(i-1, j)
        else:
            rebuild_LCS_aux(i, j-1)

    rebuild_LCS_aux(len(X), len(Y))


# SICP3.27 メモ化機能を部品化


def memoize(f, keygen):
    def memoized_f(x, y):
        key = keygen(x, y)
        if key in memo:
            return memo[key]
        memo[key] = f(x, y)
        return memo[key]

    memo = dict()
    return memoized_f


def LCS_recur(X, Y):
    """ O(mn) m:len(X), n:len(Y)
    """
    if X == [] or Y == []:
        return []
    if X[-1] == Y[-1]:
        return memoized_LCS_recur(X[:-1], Y[:-1]) + [X[-1]]
    else:
        x = memoized_LCS_recur(X[:-1], Y)
        y = memoized_LCS_recur(X, Y[:-1])
        return x if len(x) > len(y) else y


def keygen(X, Y):
    return ("".join(X), "".join(Y))


memoized_LCS_recur = memoize(LCS_recur, keygen)
