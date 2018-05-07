"""
    固定長配列によるスタック

    後入れ先出し方策を実現する動的集合。
    なるべくリストのメソッドを使わないで実装する。
    各操作の実行時間はO(1)。
"""


class FixedStack:
    def __init__(self, capacity):
        self._xs = [None] * capacity
        self._top = -1
    
    def empty(self):
        return self._top == -1
    
    def push(self, x):
        if self._top == len(self._xs) - 1:
            raise Exception("overflow")
        else:
            self._top += 1
            self._xs[self._top] = x
    
    def pop(self):
        if self.empty():
            raise Exception("underflow")
        else:
            self._top -= 1
            return self._xs[self._top + 1]