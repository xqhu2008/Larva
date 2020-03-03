#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
    dynamic_programming.py
        The demo implementation of some problem by dynamic programing algorithm
'''


def make_change(coins, change):
    mincoins = [0] * (change + 1)
    usedcoins = [0] * (change + 1)
    for cent in range(1, change + 1):
        coincount = cent
        newcoin = coins[0]
        for j in [c for c in coins if c <= cent]:
            if mincoins[cent - j] + 1 < coincount:
                coincount = mincoins[cent - j] + 1
                newcoin = j
        mincoins[cent] = coincount
        usedcoins[cent] = newcoin

    scoins = []
    coin = change
    while coin > 0:
        curcoin = usedcoins[coin]
        scoins.append(curcoin)
        coin -= curcoin

    return mincoins[change], scoins


if __name__ == "__main__":
    print(make_change([1, 5, 10, 21, 25], 73))