#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
    queue.py:
        queue data structure implementation used python
'''

import random


class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        return self._queue.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)

    def __bool__(self):
        return bool(self._queue)


class Deque:
    def __init__(self):
        self._queue = []

    def add_front(self, item):
        self._queue.insert(0, item)

    def add_rear(self, item):
        self._queue.append(item)

    def remove_front(self):
        return self._queue.pop(0)

    def remove_rear(self):
        return self._queue.pop()

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return str(self._queue)

    def __bool__(self):
        return bool(self._queue)

