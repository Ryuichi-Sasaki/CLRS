"""
    ロッド切出し問題

    長さnの金属棒と、長さ毎の金属棒の買取額リストが与えられる。  
    金属棒を切出すコストを無視できるとき、収入を最大にするには  
    どのように切出せばよいか。また、収入の最大値はいくらか。

    3つのアルゴリズムで計算する。

    ＜再帰的トップダウン方式＞
      棒の左から切り出す長さを決めていく。  
      同じ部分問題の計算が複数回発生する。

    ＜動的計画法＞
      同じ部分問題を一度しか解かないように、  
      一度解いた部分問題の解を保存しておく。

      ＜トップダウン方式＞
        大きな部分問題からとりかかる。  
        依存する小さな部分問題の解が保存されてない場合は、  
        その小さな部分問題にとりかかる。

      ＜ボトムアップ方式＞
        小さな部分問題から計算する。
        大きな部分問題を解く際には、それが依存する小さな部分問題の  
        解はすべて保存済みである。
"""


def cut_rod(p, n):
    """ θ(2^n)
    """
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    """ θ(n^2)
    """
    def memoized_cut_rod_aux(p, n, r):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = float("-inf")
            for i in range(1, n + 1):
                q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
        r[n] = q
        return q

    r = [float("-inf")] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def bottom_up_cut_rod(p, n):
    """ θ(n^2)
    """
    r = [None] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i + 1):
            q = max(q, p[j - 1] + r[i - j])
        r[i] = q
    return r[n]


def print_cut_rod_solution(p, n):
    """ θ(n^2)  
        ある最適解における、各切出し長を印字する。
    """
    def extended_bottom_up_cut_rod(p, n):
        r = [None] * (n + 1)
        s = [None] * n
        r[0] = 0
        for i in range(1, n + 1):
            q = float("-inf")
            for j in range(1, i + 1):
                if q < p[j - 1] + r[i - j]:
                    q = p[j - 1] + r[i - j]
                    s[i - 1] = j
            r[i] = q
        return (r, s)

    (_, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n - 1], end=" ")
        n -= s[n - 1]
    print()


def costed_bottom_up_cut_rod(p, n, c):
    """ θ(n^2)  
        金属棒の切出しにかかるコストを考慮する版。
    """
    r = [None] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i):   #切出すパターンのみ
            q = max(q, p[j - 1] + r[i - j] - c)
        r[i] = max(q, p[i - 1]) #切出さないパターンと比較
    return r[n]


def extended_memoized_cut_rod(p, n):
    """ θ(n^2)  
        最適解の値と共に最適解も出力する版。
    """
    def memoized_cut_rod_aux(p, n, r):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = float("-inf")
            for i in range(1, n + 1):
                prev = memoized_cut_rod_aux(p, n - i, r)
                if q < p[i - 1] + prev:
                    q = p[i - 1] + prev
                    s[n - 1] = i
        r[n] = q
        return q

    r = [float("-inf")] * (n + 1)
    s = [float("-inf")] * n
    q = memoized_cut_rod_aux(p, n, r)
    t = []
    while n > 0:
        t.append(s[n - 1])
        n -= s[n - 1]
    return (q, t)
