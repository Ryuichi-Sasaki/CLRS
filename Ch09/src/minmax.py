"""
    集合の(最小値,最大値)探索

    n要素の集合から最小値と最大値を同時に求める。

    ＜方法＞
      ・全比較
      ・対比較
    
    [全比較]
      入力要素全てに対して、最小値、最大値と比較する。
      比較回数は2n-2回。

    [対比較]
      入力を対に分割し、対の要素の大小を比較する。
      小さい方と最小値を比較、大きい方と最大値を比較する。
      入力サイズが奇数の場合、比較回数は3⌊n/2⌋回。
      入力サイズが偶数の場合、比較回数は3n/2 - 2回。
      いずれも3⌊n/2⌋以下となる。
"""


def minmax(A):
    B = list(A)
    min, max = B[0], B[0]
    for i in range(1, len(B)):
        if B[i] < min:
            min = B[i]
        if B[i] > max:
            max = B[i]
    return (min, max)


def minmax_fast(A):
    B = list(A)
    if len(B) % 2 == 0:
        if B[0] < B[1]:
            min, max = B[0], B[1]
        else:
            min, max = B[1], B[0]
        offset = 2
    else:
        min, max = B[0], B[0]
        offset = 1
    for i in range(offset, len(B), 2):
        x, y = B[i], B[i+1]
        (small, big) = (x, y) if x < y else (y, x)
        if small < min:
            min = small
        if big > max:
            max = big
    return (min, max)