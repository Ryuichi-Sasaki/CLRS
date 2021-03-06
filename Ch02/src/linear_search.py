"""
    順次探索

    ＜ループ不変式＞
      for文の各繰り返しが開始されるときには、
      A[0..i-1]にはvが見つかっていない。

    初期条件（基底）：
      i = 0 ではA[0..i-1]は存在しないので、
      vは見つかっていない。

    ループ内条件（帰納）：
      vと一致するA[i]が見つかった場合、直ちにiを返すので
      帰納は考えない。
      あるループでA[i]がvと一致しなかった場合、iに1を加えて
      次の繰り返しを行うので、ループ不変式が維持される。

    終了条件（停止）：
      for文が停止するのは、あるループでvが見つかった場合と、
      最後のループでもvが見つからなかった場合である。
      vが見つかった際にはそのときのiが返され、
      vが見つからなかった際にはNoneが返されるので、正当である。
"""


def linear_search(A, v):
    for i in range(0, len(A)):
        if A[i] == v:
            return i
    else:
        return None