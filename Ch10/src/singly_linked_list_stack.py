"""
    一方向連結リストによるスタック

    各操作の実行時間はO(1)
"""


class Item:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedStack:
    def __init__(self):
        self._head = None
        self._count = 0
    
    def _insert(self, item):
        """ O(1)
        """
        item.next = self._head
        self._head = item
    
    def _extract_head(self):
        """ O(1)
        """
        item = self._head
        self._head = self._head.next
        return item
    
    def empty(self):
        """ O(1)
        """
        return self._count == 0
    
    def push(self, x):
        """ O(1)
        """
        self._count += 1
        item = Item(x)
        self._insert(item)
    
    def pop(self):
        """ O(1)
        """
        if self.empty():
            raise Exception("underflow")
        else:
            self._count -= 1
            return self._extract_head().key
