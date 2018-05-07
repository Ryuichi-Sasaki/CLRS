import unittest
import sys
sys.path.append("../src/")
from fixed_queue import FixedQueue


class TestFixedQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = FixedQueue(6)
        q.enqueue(4)
        q.enqueue(1)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 4)
        
        q.enqueue(8)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q._xs, [4, 1, 3, 8, None, None])

    def test_overflow(self):
        q = FixedQueue(0)
        with self.assertRaises(Exception):
            q.enqueue(0)

        q = FixedQueue(1)
        q.enqueue(0)
        with self.assertRaises(Exception):
            q.enqueue(0)

    def test_underflow(self):
        q = FixedQueue(10)
        with self.assertRaises(Exception):
            q.dequeue()
        
        q.enqueue(0)
        q.dequeue()
        with self.assertRaises(Exception):
            q.dequeue()


if __name__ == "__main__":
    unittest.main()
