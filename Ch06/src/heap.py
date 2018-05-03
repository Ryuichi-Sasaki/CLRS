"""
    2分木ヒープ
"""


class Heap:
    """ 2分木ヒープ
    """
    def __init__(self, A, min=False):
        """ O(n)
        """
        comp = (lambda x, y: x < y) if min else \
               (lambda x, y: x > y)
        self._A = A
        self._size = len(A)
        self._comp = comp
        self._build_heap()
    
    def _build_heap(self):
        """ O(n)  
            ボトムアップでヒープを構築する
        """
        for i in range(len(self._A) // 2 - 1, -1, -1):
            self._heapify(i)
    
    def _heapify(self, i):
        """ O(lgn)  
            _A[i]を根とする部分木をcompに基づいたヒープにする  
            前提：_left(i)と_right(i)を根とする部分木は既にcompに基づいたヒープである
        """
        l = self._left(i)
        r = self._right(i)
        if l < self._size and self._comp(self._A[l], self._A[i]):
            found = l
        else:
            found = i
        if r < self._size and self._comp(self._A[r], self._A[found]):
            found = r
        if found != i:
            self._A[i], self._A[found] = self._A[found], self._A[i]
            self._heapify(found)

    def _parent(self, i):
        """ Θ(1)  
            親の添字を返す
        """
        return (i + 1) // 2 - 1

    def _left(self, i):
        """ Θ(1)  
            左の子の添字を返す
        """
        return (i + 1) * 2 - 1

    def _right(self, i):
        """ Θ(1)  
            右の子の添字を返す
        """
        return (i + 1) * 2
    
    def heap_sort(self):
        """ Θ(nlgn)
        """
        for i in range(len(self._A) - 1, 0, -1):
            self._A[0], self._A[i] = self._A[i], self._A[0]
            self._size -= 1
            self._heapify(0)
    
    def heap_top(self):
        """ O(1)
        """
        return self._A[0]
    
    def heap_extract_top(self):
        """ O(lgn)  
        """
        if self._size < 1:
            raise Exception("heap underflow")
        top = self._A[0]
        self._A[0] = self._A[self._size - 1]
        self._size -= 1
        self._heapify(0)
        return top

    def heap_insert(self, key):
        """ O(lgn)
        """
        e = float("inf") if self._comp(0, 1) else float("-inf")
        if self._size == len(self._A):
            self._A.append(e)
        else:
            self._A[self._size] = e
        self._size += 1
        self.heap_modify_key(self._size - 1, key)
    
    def heap_modify_key(self, i, key):
        """ O(lgn)
        """
        if self._comp(self._A[i], key):
            raise Exception("invalid key")
        self._A[i] = key
        pi = self._parent(i)
        while i > 0 and self._comp(self._A[i], self._A[pi]):
            self._A[i], self._A[pi] = self._A[pi], self._A[i]
            i, pi = pi, self._parent(pi)