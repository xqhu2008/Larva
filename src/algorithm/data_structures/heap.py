#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: heap.py
    heap data structure implementation by python language.

Author: Alex Hu
Create date: 2020 - 01 - 20    
'''


class Heap:
    def __init__(self, datas = None):
        self._initialize(datas)

    def _initialize(self, datas):
        self._heap = [0]
        if datas is not None:
            self._heap.extend(datas)
            self._build_heap()

    def size(self):
        return len(self._heap) - 1

    def __str__(self):
        return str(self._heap[1:])

    def is_empty(self):
        return self.size() == 0

    def _build_heap(self):
        i = self.size() // 2
        while i > 0:
            self._heapify(i)
            i -= 1

    @staticmethod
    def build_heap(datas):
        return Heap(datas)

    def _find_min_branch(self, i):
        if 2 * i + 1 > self.size():
            return 2 * i
        else:
            if self._heap[2 * i] < self._heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def _heapify(self, i):
        while 2 * i < self.size() + 1:
            mc = self._find_min_branch(i)
            if self._heap[mc] < self._heap[i]:
                self._heap[mc], self._heap[i] = self._heap[i], self._heap[mc]
            i = mc

    def insert(self, data):
        self._heap.append(data)
        pos = self.size()
        while pos >= 2:
            parent = pos // 2
            if self._heap[parent] > self._heap[pos]:
                self._heap[parent], self._heap[pos] = self._heap[pos], self._heap[parent]
            else:
                break

            pos = parent

    def pop(self):
        length = self.size()
        if length == 0:
            raise ValueError

        if length == 1:
            return self._heap.pop()

        retval = self._heap[1]
        self._heap[1] = self._heap.pop()
        self._heapify(1)
        return retval

    @staticmethod
    def heap_sort(datas):
        heap = Heap.build_heap(datas)
        datas = []
        while not heap.is_empty():
            datas.append(heap.pop())
        return datas


if __name__ == "__main__":
    import random

    N = 10
    datas = [random.randrange(N) for _ in range(N)]
    # datas = [1, 3, 5, 2, 4, 8, 6, 7, 9, 10]
    print(datas)
    heap = Heap.build_heap(datas)
    print(heap)
    heap.insert(12)
    heap.insert(3)
    print(heap)
    print(Heap.heap_sort(datas))