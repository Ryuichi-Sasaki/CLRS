"""
    2分探索木
"""


class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self._root = root

    def inorder_walk_recur(self):
        """ Θ(n)  
            中間順木巡回によりキーを昇順に印字する（再帰版）
        """
        self._inorder_walk_recur(self._root)

    def _inorder_walk_recur(self, x):
        if x != None:
            self._inorder_walk_recur(x.left)
            print(x.key)
            self._inorder_walk_recur(x.right)

    def inorder_walk_iter(self):
        """ Θ(n)  
            中間順木巡回によりキーを昇順に印字する（反復版）
        """
        stack = [self._root]
        visited = []
        while stack != []:
            x = stack.pop()
            if x == None:
                continue
            if visited != [] and visited[-1] == x:
                print(x.key)
                visited.pop()
                continue
            stack.append(x.right)
            stack.append(x)
            stack.append(x.left)
            visited.append(x)

    def search_recur(self, x, k):
        """ O(h)  
            与えられた部分木からキーがkである節点を探索する（再帰版）
        """
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search_recur(x.left, k)
        else:
            return self.search_recur(x.right, k)

    def search_iter(self, x, k):
        """ O(h)  
            与えられた部分木からキーがkである節点を探索する（反復版）
        """
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum_iter(self, x):
        """ O(h)  
            与えられた部分木の最小要素を返す（反復版）
        """
        while x.left != None:
            x = x.left
        return x

    def minimum_recur(self, x):
        """ O(h)  
            与えられた部分木の最小要素を返す（再帰版）
        """
        if x.left == None:
            return x
        return self.minimum_recur(x.left)

    def maximum_iter(self, x):
        """ O(h)  
            与えられた部分木の最大要素を返す（反復版）
        """
        while x.right != None:
            x = x.right
        return x

    def maximum_recur(self, x):
        """ O(h)  
            与えられた部分木の最大要素を返す（再帰版）
        """
        if x.right == None:
            return x
        return self.maximum_recur(x.right)

    def successor(self, x):
        """ O(h)  
            与えられた節点よりも大きい最小の節点を返す
        """
        if x.right != None:
            return self.minimum_iter(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        """ O(h)  
            与えられた節点よりも小さい最大の節点を返す
        """
        if x.left != None:
            return self.maximum_iter(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    def insert_iter(self, z):
        """  O(h)  
             与えられた節点を適切な位置に挿入する（反復版）
        """
        y = None
        x = self._root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def insert_recur(self, z):
        """  O(h)  
             与えられた節点を適切な位置に挿入する（再帰版）
        """
        self._insert_recur(None, self._root, z)

    def _insert_recur(self, y, x, z):
        if x != None:
            if z.key < x.key:
                self._insert_recur(x, x.left, z)
            else:
                self._insert_recur(x, x.right, z)
        else:
            z.parent = y
            if y == None:
                self._root = z
            elif z.key < y.key:
                y.left = z
            else:
                y.right = z

    def _transplant(self, u, v):
        if u.parent == None:
            self._root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def delete(self, z):
        """ O(h)  
            与えられた節点を削除し、木を再構成する
        """
        if z.left == None:
            self._transplant(z, z.right)
        elif z.right == None:
            self._transplant(z, z.left)
        else:
            y = self.minimum_iter(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
