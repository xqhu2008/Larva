#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: math_paper.py
    This module implements an automatic generation of mathematics test paper for the first
    grade of the primary school.

Author: Alex Hu
Create date: 2020 - 02 - 18    
'''


import random


class Subject:
    def __init__(self, operands, operators, result):
        self._operands = operands[:]
        self._operators = operators[:]
        self._result = result

    def __str__(self):
        subject = str(self._operands[0])
        for index, val in enumerate(self._operators):
            subject += f"{self._operators[index]} {self._operands[index + 1]}"

        subject += f" = {self._result}"

        return subject

    def __eq__(self, other):
        return str(self) == str(other)

    def __len__(self):
        return len(self._operands)

    def get_operands(self):
        return self._operands

    def get_operators(self):
        return self._operators

    def get_result(self):
        return self._result

    def get_subject(self):
        return self._operands, self._operators, self._result

    def format_subject(self, **style):
        parentheses = style["parentheses"]
        digit_size = style["digit_size"]
        show_result = style["show_result"]

        subject_str = self._format_operand(0, parentheses == 0, digit_size)
        for index, value in enumerate(self._operators):
            subject_str += f" {value} " + self._format_operand(index + 1, parentheses == index + 1, digit_size)

        subject_str += " = "
        subject_str += self._format_result(show_result, digit_size)

        return subject_str

    def _format_operand(self, index, substitute = False, length = 2):
        format_str = "{:>" + str(length) + "} "
        return format_str.format(self._operands[index]) if not substitute else "(    )"

    def _format_result(self, substitute = True, length = 2):
        format_str = "{:>" + str(length) + "} "
        return format_str.format(self._result) if substitute else "    "


class MathPaper:
    def __init__(self, max_int = 20):
        self._max_int = max_int
        self._subjects = []
        self._initialize()

    def _initialize(self):
        self._templates2 = []
        self._templates3 = []

        for m in range(1, self._max_int):
            for n in range(1,self._max_int):
                if m + n <= self._max_int:
                    self._templates2.append(Subject([m, n], ['+'], m + n))
                    for l in range(1, self._max_int):
                        if m + n + l < self._max_int:
                            self._templates3.append(Subject([m, n, l], ['+', '+'], m + n + l))
                        elif m + n - l >= 0:
                            self._templates3.append(Subject([m, n, l], ['+', '-'], m + n - l))
                elif m - n >= 0:
                    self._templates2.append(Subject([m, n], ['-'], m - n))
                    for l in range(1, self._max_int):
                        if m - n + l < self._max_int:
                            self._templates3.append(Subject([m, n, l], ['-', '+'], m - n + l))
                        elif m - n - l >= 0:
                            self._templates3.append(Subject([m, n, l], ['-', '-'], m - n - l))

    def generate_paper(self, binary = 80,  ternary = 20):
        binary_pos = random.randrange(len(self._templates2) - binary)
        ternary_pos = random.randrange(len(self._templates3) - ternary)
        random.shuffle(self._templates2)
        random.shuffle(self._templates3)
        self._subjects = self._templates2[binary_pos : binary_pos + binary]
        self._subjects.extend(self._templates3[ternary_pos : ternary_pos + ternary])
        return self._subjects

    def get_subjects(self, type = 'all'):
        if type == 'all':
            return self._subjects[:]
        elif type == "binary":
            return [subject for subject in self._subjects if len(subject) == 2]
        elif type == "ternary":
            return [subject for subject in self._subjects if len(subject) == 3]
        else:
            return []

    def __len__(self):
        return len(self._subjects)

    def format_paper(self, columns = 4):
        formatted_subjects = []
        for subject in self.get_subjects('binary'):
            formatted_subjects.append(subject.format_subject(parentheses = -1, digit_size = 2, show_result = False))

        subjects = self.get_subjects('ternary')
        for subject in subjects[:len(subjects) // 2]:
            formatted_subjects.append(subject.format_subject(parentheses = -1, digit_size = 2, show_result = False))

        for subject in subjects[len(subjects) //  2:]:
            formatted_subjects.append(subject.format_subject(parentheses = random.randrange(len(subject)), \
                                                             digit_size = 2, show_result = True))

        subjects_reuslt = []
        rows = len(self) // columns
        for i in range(rows):
            subject_str = ""
            for j in range(columns):
                subject_str += formatted_subjects[i + j * rows] + "        "
            subjects_reuslt.append(subject_str)

        return subjects_reuslt


if __name__ == "__main__":
    paper = MathPaper()
    paper.generate_paper()
    subjects = paper.format_paper()
    for subject in subjects:
        print(subject)