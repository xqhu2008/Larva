#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'''
    stack.py:
        stack abstract data structure implementation used by python
'''


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __bool__(self):
        return bool(self._items)

