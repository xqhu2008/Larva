# -*- encoding:utf-8 -*-
'''
    sudoku.py:
        sudoku game implementation by python. This implementation includes game solution and generation.
'''


class Sudoku:
    def __init__(self, rows = 3, cols = 3):
        self._rows = rows * rows
        self._cols = cols * cols
        self._fields = [0 for _ in range(self._rows) for _ in range(self._cols)]

    def loadFromFile(self, fileName):
        pass

    def doSudoku(self):
        pass

