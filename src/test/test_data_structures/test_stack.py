#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: test_stack.py

Author: Alex Hu
Create date: 2020/1/11    
'''

from algorithm.data_structures.stack import Stack


def matches(op, cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl)


def bracket_match(symstring):
    p = Stack()
    for s in symstring:
        if s in "{[(":
            p.push(s)
        elif s in ")]}":
            if p.is_empty():
                return False
            else:
                top = p.pop()
                if not matches(top, s):
                    return False
    else:
        return p.is_empty()


def base_covert(num, base = 2):
    digits = '0123456789ABCDEF'

    data = Stack()

    while num > 0:
        data.push(num % base)
        num = num // base

    output = ""
    while not data.is_empty():
        output += digits[data.pop()]

    return output


def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opstack = Stack()
    postfix = []

    for token in infixexpr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfix.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.is_empty()) and (prec[opstack.peek()] >= prec[token]):
                postfix.append(opstack.pop())
            opstack.push(token)

    while not opstack.is_empty():
        postfix.append(opstack.pop())

    return ''.join(postfix)


def envaluate_postfix(postfixexpr):
    oprand = Stack()
    for token in postfixexpr:
        if token in "0123456789":
            oprand.push(token)
        else:
            result = do_math(token, oprand.pop(), oprand.pop())
            oprand.push(result)

    return oprand.pop()


def do_math(op, op2, op1):
    if op == "*":
        return int(op1) * int(op2)
    elif op == "/":
        return int(op1) / int(op2)
    elif op == "+":
        return int(op1) + int(op2)
    else:
        return int(op1) - int(op2)


if __name__ == "__main__":
    # print(bracket_match("((()))(())"))
    # print(bracket_match("(()"))
    # print(bracket_match("(()))"))
    # print(base_covert(100, 16))

    print(infix_to_postfix('A+B*C'))
    print(envaluate_postfix('345*+'))
