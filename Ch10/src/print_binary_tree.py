"""
    2分木を印字する手続き
"""


class Node:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def print_recur(root):
    if root != None:
        print(root.key)
        print_recur(root.left)
        print_recur(root.right)


def print_iter(root):
    stack = [root]
    while stack != []:
        node = stack.pop()
        print(node.key)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)