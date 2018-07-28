"""
    動的計画法によりn番目のフィボナッチ数を求める
"""


def fib(n):
    """ モデル実装
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def memoized_fib(n):
    """ θ(n)
    """
    def memoized_fib_aux(n):
        if memo[n] != None:
            return memo[n]
        if memo[n - 1] == None:
            memo[n - 1] = memoized_fib_aux(n - 1)
        return memo[n - 1] + memo[n - 2]

    memo = [0, 1] + [None] * (n - 1)
    return memoized_fib_aux(n)


def bottom_up_fib(n):
    """ θ(n)
    """
    fibs = [0,1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]


#### SICP3.27より、メモ化機能を部品化する


def memoize(f):
    memo = dict()
    def memoized_f(input):
        if input in memo:
            return memo[input]
        memo[input] = f(input)
        return memo[input]
    return memoized_f


def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fib2(n - 1) + memoized_fib2(n - 2)


memoized_fib2 = memoize(fib2)
