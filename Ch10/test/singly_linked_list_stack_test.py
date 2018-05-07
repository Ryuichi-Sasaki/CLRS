import unittest
import sys
sys.path.append("../src/")
from singly_linked_list_stack import SinglyLinkedStack


class TestSinglyLinkedStack(unittest.TestCase):
    def test_empty(self):
        s = SinglyLinkedStack()
        self.assertTrue(s.empty())

        s.push(0)
        self.assertFalse(s.empty())

        s.pop()
        self.assertTrue(s.empty())

    def test_push_pop(self):
        s = SinglyLinkedStack()
        s.push(0)
        self.assertEqual(0, s.pop())

        s.push(1)
        s.push(2)
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())

    def test_underflow(self):
        s = SinglyLinkedStack()
        with self.assertRaises(Exception):
            s.pop()

        s.push(0)
        s.pop()
        with self.assertRaises(Exception):
            s.pop()


if __name__ == "__main__":
    unittest.main()
