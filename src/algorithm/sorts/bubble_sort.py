#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: bubble_sort.py
    This module is the python language implementation of bubble sort algorithm.

Author: Alex Hu
Create date: 2020/1/9    
'''


def bubble_sort(datas):
    length = len(datas)
    last = length - 1
    for i in range(length - 1):
        finished = True
        for j in range(last):
            if datas[j + 1] < datas[j]:
                datas[j + 1], datas[j] = datas[j], datas[j + 1]
                finished = False
                last = j

        if finished:
            break

    return datas

