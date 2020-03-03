# -*- encoding:utf-8 -*-
# !/usr/bin/env python
'''
    recursion.py:
        demo the recursion solution of some problem
'''

import sys
import turtle

def sum_list(numlst):
    if len(numlst) == 1:
        return numlst[0]
    elif len(numlst) == 0:
        return 0
    else:
        return numlst[0] + sum_list(numlst[1:])


def binary_conversion(num, base):
    binarys = "0123456789ABCDEF"

    if num < base:
        return binarys[num]
    else:
        return binary_conversion(num // base, base) + binarys[num % base]

def tell_story():
    print("Once upon a time, there is a mountain")
    tell_story()


def drawspiral(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawspiral(t, linelen - 5)


def tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(t, branch_len - 15)
        t.left(40)
        tree(t, branch_len - 15)
        t.right(20)
        t.backward(branch_len)


def change_money(coins, change, knowns):
    min_coins = change
    if change in coins:
        knowns[change] = 1
        return 1
    elif knowns[change] > 0:
        return knowns[change]
    else:
        for i in [c for c in coins if c <= change]:
            num_coins = 1 + change_money(coins, change - i, knowns)
            if num_coins < min_coins:
                min_coins = num_coins
                knowns[change] = min_coins
    return min_coins


if __name__ == "__main__":
    # print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # print(binary_conversion(255, 16))
    # print(binary_conversion(256, 16))
    # # tell_story()
    # print(sys.getrecursionlimit())
    #
    # t = turtle.Turtle()
    # # drawspiral(t, 100)
    # t.left(90)
    # t.penup()
    # t.backward(100)
    # t.pendown()
    # t.pencolor('green')
    # t.pensize(2)
    # tree(t, 75)
    # t.hideturtle()
    #
    # turtle.done()

    print(change_money([1, 5, 10, 21, 25], 63, [0] * 64))