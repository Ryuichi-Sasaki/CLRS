import unittest
import sys
sys.path.append("../src/")
from fixed_double_ended_queue import FixedDoubleEndedQueue
from random import randint


class TestFixedQueue(unittest.TestCase):
    def test_push_pop(self):
        q = FixedDoubleEndedQueue(6)
        q.push_left(1)
        q.push_left(2)
        self.assertEqual(2, q.pop_left())
        self.assertEqual(1, q.pop_left())

        q.push_right(3)
        q.push_right(4)
        self.assertEqual(4, q.pop_right())
        self.assertEqual(3, q.pop_right())

        q.push_left(5)
        self.assertEqual(5, q.pop_right())

        q.push_right(6)
        self.assertEqual(6, q.pop_left())


    def test_overflow(self):
        q = FixedDoubleEndedQueue(0)
        with self.assertRaises(Exception):
            q.push_left(0)
        with self.assertRaises(Exception):
            q.push_right(0)

        q = FixedDoubleEndedQueue(1)
        q.push_left(0)
        with self.assertRaises(Exception):
            q.push_left(0)
        with self.assertRaises(Exception):
            q.push_right(0)

        q = FixedDoubleEndedQueue(1)
        q.push_right(0)
        with self.assertRaises(Exception):
            q.push_left(0)
        with self.assertRaises(Exception):
            q.push_right(0)

    def test_underflow(self):
        q = FixedDoubleEndedQueue(10)
        with self.assertRaises(Exception):
            q.pop_left()
        with self.assertRaises(Exception):
            q.pop_right()
        
        q.push_left(0)
        q.pop_left()
        with self.assertRaises(Exception):
            q.pop_left()
        with self.assertRaises(Exception):
            q.pop_right()
        
        q.push_left(0)
        q.pop_right()
        with self.assertRaises(Exception):
            q.pop_left()
        with self.assertRaises(Exception):
            q.pop_right()
        
        q.push_right(0)
        q.pop_left()
        with self.assertRaises(Exception):
            q.pop_left()
        with self.assertRaises(Exception):
            q.pop_right()

        q.push_right(0)
        q.pop_right()
        with self.assertRaises(Exception):
            q.pop_left()
        with self.assertRaises(Exception):
            q.pop_right()


if __name__ == "__main__":
    unittest.main()
