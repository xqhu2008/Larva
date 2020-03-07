#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: shell_sort.py
    This module implements the shell sort algorithm.

Author: Alex Hu
Create date: 2020 - 03 - 07    
'''


def shell_sort(datas):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(datas):
            temp = datas[i]
            j = i
            while j >= gap and datas[j - gap] > temp:
                datas[j] = datas[j - gap]
                j -= gap
            datas[j] = temp
            i += 1

    return datas

