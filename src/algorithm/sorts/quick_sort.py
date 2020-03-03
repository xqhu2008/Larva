#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: quick_sort.py
    This module implements the quick sort algorithm.

Author: Alex Hu
Create date: 2020/1/11    
'''


def partition(datas, lo, ho):
    i, j = lo, ho
    pivot = lo
    while i != j:
        while i < j and datas[pivot] < datas[j]:
            j -= 1

        while i < j and datas[pivot] >= datas[i]:
            i += 1

        if i < j:
            datas[i], datas[j] = datas[j], datas[i]

    datas[i], datas[pivot] = datas[pivot], datas[i]
    return i


def quick_sort(datas, lo = 0, ho = None):
    if ho is None:
        ho = len(datas) - 1

    length = ho - lo + 1
    if length <= 1:
        return datas

    pivot = partition(datas, lo, ho)
    quick_sort(datas, lo, pivot - 1)
    quick_sort(datas, pivot + 1, ho)
    return datas


# def quick_sort(datas):
#     if len(datas) <= 1:
#         return datas
#
#     pivot = 0
#     left = []
#     right = []
#     for i in range(1, len(datas)):
#         if datas[i] < datas[pivot]:
#             left.append(datas[i])
#         else:
#             right.append(datas[i])
#
#     return quick_sort(left) + [datas[pivot]] + quick_sort(right)

