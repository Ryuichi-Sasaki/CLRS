"""
    一方向循環リストによる辞書操作

    番兵を用いている。
"""


class Item:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedDictionary:
    def __init__(self):
        self._nil = Item(None)
        self._nil.next = self._nil
    
    def search(self, k):
        """ O(n)
        """
        self._nil.key = k
        x = self._nil.next
        while x.key != k:
            x = x.next
        return x if x != self._nil else None
    
    def insert(self, x):
        """ O(1)
            キー値は重複しないものと仮定。
        """
        x.next = self._nil.next
        self._nil.next = x
    
    def delete(self, x):
        """ O(n)
            辞書内に指定された要素が存在すると仮定。
        """
        y = self._nil
        while y.next != x:
            y = y.next
        y.next = x.next