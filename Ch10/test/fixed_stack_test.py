import unittest
import sys
sys.path.append("../src/")
from fixed_stack import FixedStack
from random import randint


class TestFixedStack(unittest.TestCase):
    def test_empty(self):
        s = FixedStack(10)
        self.assertTrue(s.empty())

        s.push(randint(0, 100))
        self.assertFalse(s.empty())
        
        s.pop()
        self.assertTrue(s.empty())

    def test_push_pop(self):
        num_push = randint(0, 100)
        num_pop  = randint(0, num_push)
        s1, s2 = [], FixedStack(100)
        for _ in range(num_push):
            e = randint(0, 30)
            s1.append(e)
            s2.push(e)
        for _ in range(num_pop):
            s1.pop()
            s2.pop()
        self.assertEqual(s1, s2._xs[:s2._top + 1])
    
    def test_overflow(self):
        s = FixedStack(0)
        with self.assertRaises(Exception):
            s.push(0)

        s = FixedStack(1)
        s.push(0)
        with self.assertRaises(Exception):
            s.push(0)

    def test_underflow(self):
        s = FixedStack(10)
        with self.assertRaises(Exception):
            s.pop()

        s.push(0)
        s.pop()
        with self.assertRaises(Exception):
            s.pop()


if __name__ == "__main__":
    unittest.main()
