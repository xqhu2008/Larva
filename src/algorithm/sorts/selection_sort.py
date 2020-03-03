#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: selection_sort.py
    This module is the python language implementation of selection sort algorithm.

Author: Alex Hu
Create date: 2020/1/9
'''


def selection_sort(datas):
    length = len(datas)
    for i in range(length):
        pos = i
        for j in range(i, length):
            if datas[j] < datas[pos]:
                pos = j
        datas[i], datas[pos] = datas[pos], datas[i]

    return datas
