#-*- encoding:utf-8 -*-
'''
    shuxue.py
'''

import random


class MathExercise:
    def __init__(self, scope = 20):
        self._subjects = []
        self._answers = []
        self._scope = scope

    def buildIssues(self, counts = 500):
        signs = ['+', '-']
        nums = [1 + i for i in range(self._scope)]

        while len(self._subjects) < counts:
            op1 = random.choice(nums)
            op2 = random.choice(nums)
            sign = random.choice(signs)
            if sign == '+':
                if op1 + op2 <= 20 and (op1, sign, op2) not in self._subjects:
                    self._subjects.append((op1, sign, op2))
                    self._answers.append(op1 + op2)
            else:
                if op1 > op2 and (op1, sign, op2) not in self._subjects:
                    self._subjects.append((op1, sign, op2))
                    self._answers.append(op1 - op2)

    def printExercise(self):
        for op1, sign, op2 in self._subjects:
            print("{: >2d} {} {: >2d} = ".format(op1, sign, op2))

    def printAnswers(self):
        for i in range(len(self._subjects)):
            op1, sign, op2 = self._subjects[i]
            print("{: >2d} {} {: >2d} = {}".format(op1, sign, op2, self._answers[i]))


if __name__ == "__main__":
    exercise = MathExercise()
    exercise.buildIssues()
    exercise.printExercise()
    exercise.printAnswers()
