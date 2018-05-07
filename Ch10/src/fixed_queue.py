"""
    固定長配列によるキュー

    先入れ先出し方策を実現する動的集合。
    なるべくリストのメソッドを使わないで実装する。
    各操作の実行時間はO(1)。    
"""


class FixedQueue:
    def __init__(self, capacity):
        self._xs = [None] * capacity
        self._head = 0
        self._tail = 0
        self._count = 0
    
    def _empty(self):
        return self._count == 0

    def _full(self):
        return self._count == len(self._xs)

    def _prev(self, i):
        return (i - 1) % len(self._xs)

    def _next(self, i):
        return (i + 1) % len(self._xs)
    
    def enqueue(self, x):
        if self._full():
            raise Exception("overflow")
        else:
            self._xs[self._tail] = x
            self._tail = self._next(self._tail)
            self._count += 1
    
    def dequeue(self):
        if self._empty():
            raise Exception("underflow")
        else:
            self._head = self._next(self._head)
            self._count -= 1
            return self._xs[self._prev(self._head)]
