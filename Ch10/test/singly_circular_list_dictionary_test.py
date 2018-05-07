import unittest
import sys
sys.path.append("../src/")
from singly_circular_list_dictionary import SinglyLinkedDictionary
from singly_circular_list_dictionary import Item


class TestSinglyLinkedDictionary(unittest.TestCase):
    def test_insert_search(self):
        d = SinglyLinkedDictionary()
        self.assertEqual(None, d.search(0))

        x = Item(0)
        d.insert(x)
        self.assertEqual(x, d.search(0))

        y = Item(1)
        d.insert(y)
        self.assertEqual(x, d.search(0))
        self.assertEqual(y, d.search(1))
        self.assertEqual(None, d.search(2))

    def test_delete_search(self):
        d = SinglyLinkedDictionary()
        w = Item(0)
        d.insert(w)
        d.delete(w)
        self.assertEqual(None, d.search(0))

        x = Item(1)
        y = Item(2)
        z = Item(3)
        d.insert(x)
        d.insert(y)
        d.insert(z)
        d.delete(y)
        self.assertEqual(x, d.search(1))
        self.assertEqual(None, d.search(2))
        self.assertEqual(z, d.search(3))

        d.delete(x)
        self.assertEqual(None, d.search(1))
        self.assertEqual(None, d.search(2))
        self.assertEqual(z, d.search(3))

        d.delete(z)
        self.assertEqual(None, d.search(1))
        self.assertEqual(None, d.search(2))
        self.assertEqual(None, d.search(3))


if __name__ == "__main__":
    unittest.main()