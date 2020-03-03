# -*- encoding:utf-8 -*-
'''
    fibonacci.py:
        using dynamic program algorithm to solving the fibonacci problem
'''


def fibonacci(n):
    f0 = 1
    f1 = 1

    if n == 0 or n == 1:
        return f1

    for k in range(2, n + 1):
        f1, f0 = f0 + f1, f1

    return f1


def stairs(n):
    count = [0 for _ in range(n)]

    if n <= 2:
        return 1

    count[0] = 1
    count[1] = 1
    count[2] = 2

    for i in range(3, n):
        count[i] = count[i - 1] + count[i - 3]

    return count[-1]


if __name__ == "__main__":
    # print(fibonacci(0))
    print(stairs(2))
    print(stairs(3))
    print(stairs(4))
    print(stairs(50))
