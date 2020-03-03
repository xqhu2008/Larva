#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: merge_sort.py
    This module is the python language implementation of merge sort algorithm. The recursive method
    is used in the implementation.

Author: Alex Hu
Create date: 2020/1/9
'''


def merge_sort(datas):
    if len(datas) <= 1:
        return datas

    left = merge_sort(datas[:len(datas) // 2])
    right = merge_sort(datas[len(datas) // 2:])

    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return merged + left + right
