import unittest
import sys
sys.path.append("../src/")
from heap import Heap
from random import randint
from heapq import heappush


class TestHeap(unittest.TestCase):
    def test_heap_sort(self):
        B = [randint(-10, 10) for _ in range(10)]
        Heap(B, min=False).heap_sort()
        A = sorted(B)
        self.assertEqual(A, B)

    def test_heap_sort_reverse(self):
        B = [randint(-10, 10) for _ in range(10)]
        Heap(B, min=True).heap_sort()
        A = list(sorted(B, reverse=True))
        self.assertEqual(A, B)

    def test_heap_insert(self):
        A = [randint(-10, 10) for _ in range(10)]
        B, C = [], []
        heap = Heap(B, min=True)
        for n in A:
            heap.heap_insert(n)
            heappush(C, n)
        self.assertEqual(B, C)


if __name__ == "__main__":
    unittest.main()
