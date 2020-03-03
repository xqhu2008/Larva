#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: insertion_sort.py
    This module is the python language implementation of insertion sort algorithm.

Author: Alex Hu
Create date: 2020/1/9    
'''


def insertion_sort(datas):
    length = len(datas)
    for i in range(1, length):
        for j in range(i):
            if datas[i - j] < datas[i - j - 1]:
                datas[i - j], datas[i - j - 1] = datas[i - j - 1], datas[i - j]
            else:
                break

    return datas

