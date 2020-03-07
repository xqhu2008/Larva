#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name:

Author: Alex Hu
Create date: 2020/1/10    
'''

import random
import time

from algorithm.sorts.bubble_sort import bubble_sort
from algorithm.sorts.merge_sort import merge_sort
from algorithm.sorts.insertion_sort import insertion_sort
from algorithm.sorts.selection_sort import selection_sort
from algorithm.sorts.quick_sort import quick_sort
from algorithm.sorts.shell_sort import shell_sort


def time_measurement(func):
    def wrap(N, fn):
        datas = [random.randrange(N) for _ in range(N)]
        start = time.time()
        datas = func(datas, fn)
        print("Running timer: {:5f} - Function Name : {}".format(time.time() - start, fn.__name__))
        return datas

    return wrap

@time_measurement
def test_sort(datas, func):
    return func(datas)


if __name__ == "__main__":
    # test_sort(10000, bubble_sort)
    # test_sort(10000, merge_sort)
    # test_sort(10000, insertion_sort)
    # test_sort(10000, selection_sort)
    # print(test_sort(10, quick_sort))
    # test_sort(10000, quick_sort)
    print(test_sort(10, shell_sort))
    test_sort(10000, shell_sort)