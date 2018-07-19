import unittest
import sys
sys.path.append("../src/")
from binary_search_tree import Node
from binary_search_tree import BinarySearchTree
from io import StringIO


class TestBinarySearchTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bst1_node1 = Node(6)
        cls.bst1_node2 = Node(5, cls.bst1_node1)
        cls.bst1_node3 = Node(7, cls.bst1_node1)
        cls.bst1_node4 = Node(2, cls.bst1_node2)
        cls.bst1_node5 = Node(5, cls.bst1_node2)
        cls.bst1_node6 = Node(8, cls.bst1_node3)
        cls.bst1_node1.left = cls.bst1_node2
        cls.bst1_node1.right = cls.bst1_node3
        cls.bst1_node2.left = cls.bst1_node4
        cls.bst1_node2.right = cls.bst1_node5
        cls.bst1_node3.right = cls.bst1_node6
        cls.bst1 = BinarySearchTree(cls.bst1_node1)
        cls.bst1_inorder_str = "2\n5\n5\n6\n7\n8\n"

        cls.bst2_node1 = Node(2)
        cls.bst2_node2 = Node(5, cls.bst2_node1)
        cls.bst2_node3 = Node(7, cls.bst2_node2)
        cls.bst2_node4 = Node(6, cls.bst2_node3)
        cls.bst2_node5 = Node(8, cls.bst2_node3)
        cls.bst2_node6 = Node(5, cls.bst2_node4)
        cls.bst2_node1.right = cls.bst2_node2
        cls.bst2_node2.right = cls.bst2_node3
        cls.bst2_node3.left = cls.bst2_node4
        cls.bst2_node3.right = cls.bst2_node5
        cls.bst2_node4.left = cls.bst2_node6
        cls.bst2 = BinarySearchTree(cls.bst2_node1)
        cls.bst2_inorder_str = "2\n5\n5\n6\n7\n8\n"

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # 標準出力系のテストはバッファのクリアが必要なため小分けにした
    def test_inorder_walk_recur_bst1(self):
        self.bst1.inorder_walk_recur()
        self.assertEqual(self.captor.getvalue(), self.bst1_inorder_str)

    def test_inorder_walk_recur_bst2(self):
        self.bst2.inorder_walk_recur()
        self.assertEqual(self.captor.getvalue(), self.bst2_inorder_str)

    def test_inorder_walk_iter_bst1(self):
        self.bst1.inorder_walk_iter()
        self.assertEqual(self.captor.getvalue(), self.bst1_inorder_str)

    def test_inorder_walk_iter_bst2(self):
        self.bst2.inorder_walk_iter()
        self.assertEqual(self.captor.getvalue(), self.bst2_inorder_str)

    def test_search(self):
        self.assertEqual(None,            self.bst1.search_recur(self.bst1_node1, 10))
        self.assertEqual(None,            self.bst2.search_recur(self.bst2_node1, 10))
        self.assertEqual(self.bst1_node1, self.bst1.search_recur(self.bst1_node1, 6))
        self.assertEqual(self.bst2_node1, self.bst2.search_recur(self.bst2_node1, 2))
        self.assertEqual(self.bst1_node6, self.bst1.search_recur(self.bst1_node1, 8))
        self.assertEqual(self.bst2_node5, self.bst2.search_recur(self.bst2_node1, 8))

        self.assertEqual(None,            self.bst1.search_iter(self.bst1_node1, 10))
        self.assertEqual(None,            self.bst2.search_iter(self.bst2_node1, 10))
        self.assertEqual(self.bst1_node1, self.bst1.search_iter(self.bst1_node1, 6))
        self.assertEqual(self.bst2_node1, self.bst2.search_iter(self.bst2_node1, 2))
        self.assertEqual(self.bst1_node6, self.bst1.search_iter(self.bst1_node1, 8))
        self.assertEqual(self.bst2_node5, self.bst2.search_iter(self.bst2_node1, 8))

    def test_minimum(self):
        self.assertEqual(self.bst1_node4, self.bst1.minimum_iter(self.bst1_node1))
        self.assertEqual(self.bst1_node4, self.bst1.minimum_iter(self.bst1_node2))
        self.assertEqual(self.bst2_node1, self.bst2.minimum_iter(self.bst2_node1))
        self.assertEqual(self.bst2_node6, self.bst1.minimum_iter(self.bst2_node3))

        self.assertEqual(self.bst1_node4, self.bst1.minimum_recur(self.bst1_node1))
        self.assertEqual(self.bst1_node4, self.bst1.minimum_recur(self.bst1_node2))
        self.assertEqual(self.bst2_node1, self.bst2.minimum_recur(self.bst2_node1))
        self.assertEqual(self.bst2_node6, self.bst1.minimum_recur(self.bst2_node3))

    def test_maximum(self):
        self.assertEqual(self.bst1_node6, self.bst1.maximum_iter(self.bst1_node1))
        self.assertEqual(self.bst1_node5, self.bst1.maximum_iter(self.bst1_node2))
        self.assertEqual(self.bst2_node5, self.bst2.maximum_iter(self.bst2_node1))
        self.assertEqual(self.bst2_node5, self.bst1.maximum_iter(self.bst2_node3))

        self.assertEqual(self.bst1_node6, self.bst1.maximum_recur(self.bst1_node1))
        self.assertEqual(self.bst1_node5, self.bst1.maximum_recur(self.bst1_node2))
        self.assertEqual(self.bst2_node5, self.bst2.maximum_recur(self.bst2_node1))
        self.assertEqual(self.bst2_node5, self.bst1.maximum_recur(self.bst2_node3))

    def test_successor(self):
        self.assertEqual(None, self.bst1.successor(self.bst1_node6))
        self.assertEqual(None, self.bst2.successor(self.bst2_node5))

        self.assertEqual(self.bst1_node1, self.bst1.successor(self.bst1_node5))
        self.assertEqual(self.bst1_node3, self.bst1.successor(self.bst1_node1))
        self.assertEqual(self.bst2_node2, self.bst2.successor(self.bst2_node1))
        self.assertEqual(self.bst2_node4, self.bst2.successor(self.bst2_node6))

    def test_predecessor(self):
        self.assertEqual(None, self.bst1.predecessor(self.bst1_node4))
        self.assertEqual(None, self.bst2.predecessor(self.bst2_node1))

        self.assertEqual(self.bst1_node5, self.bst1.predecessor(self.bst1_node1))
        self.assertEqual(self.bst1_node1, self.bst1.predecessor(self.bst1_node3))
        self.assertEqual(self.bst2_node3, self.bst2.predecessor(self.bst2_node5))
        self.assertEqual(self.bst2_node2, self.bst2.predecessor(self.bst2_node6))


if __name__ == "__main__":
    unittest.main()
