from itertools import product


class SudokuCell:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        if value == "_":
            self.value = [str(x) for x in range(1, 10)]
            self.state = "empty"
        else:
            self.value = [value]
            self.state = "init"

    def __str__(self):
        print_str = "SudokuCell Details:\n\tRow: {}\n\tCol: {}\n\tValues: {}\n\tState: {}\n".format(self.row, self.col,
                                                                                                    self.value,
                                                                                                    self.state)
        return print_str

    def __repr__(self):
        value = "_" if len(self.value) > 1 else self.value
        repr_str = "SudokuCell({}, {}, '{}')".format(self.row, self.col, value[0])
        return repr_str

    def pop(self, number):
        '''If the number is present in the value list, remove it from the value list'''
        if number in self.value and len(self.value) > 1:
            self.value.pop(self.value.index(number))
        return None


class SudokuRow:
    '''Create a class with a list of SudokuCells.
    Create __init__, __repr__ and __str__
    '''

    def __init__(self, row, values):
        self.row = row
        self._values = values
        self.cells = [SudokuCell(row, idx, values[i]) for idx, i in enumerate(range(9))]

    def __repr__(self):
        return "SudokuRow({}, '{}')".format(self.row, self._values)

    def __str__(self):
        print_str = "|".join([" " if c == "_" else c for c in self._values])
        print_str = ("SudokuRow Details:\n\tRow: {}\n\tValues: {}"
                     .format(self.row, print_str))
        return print_str


class SudokuGrid:
    CENTER_CELLS = [1, 4, 7]

    def __init__(self, values):
        self.rows = []
        self._values = values
        for row, rvalue in enumerate(values.split("\n")):
            self.rows.append(SudokuRow(row, rvalue))

    def __repr__(self):
        return "SudokuGrid('{}')".format(self._values)

    def __str__(self):
        print_str = ""
        for row, rvalue in enumerate(self._values.split("\n")):
            temp_str = rvalue[:3] + '|' + rvalue[3:6] + '|' + rvalue[6:]
            temp_str = temp_str.replace("_", " ")
            if ((row + 1) % 3) == 0:
                temp_str = temp_str + "\n" + "-" * 11 + "\n"
            else:
                temp_str = temp_str + "\n"

            print_str = print_str + temp_str

        print_str = "SudokuGrid:\n{}".format(print_str)
        return print_str

    def getRowCells(self, row):
        return self.rows[row].cells

    def getColCells(self, col):
        cells = [self.rows[i].cells[col] for i in range(9)]
        return cells

    @staticmethod
    def getSquareCentre(row, col):
        for r, c in product(SudokuGrid.CENTER_CELLS, repeat=2):
            if abs(row - r) <= 1 and abs(col - c) <= 1:
                return r, c

    def getCell(self, row, col):
        return self.rows[row].cells[col]

    def getSquareCells(self, row, col):
        center_row, center_col = SudokuGrid.getSquareCentre(row, col)
        return [self.getCell(cell_row, cell_col) for cell_row in range(center_row - 1, center_row + 2)
                for cell_col in range(center_col - 1, center_col + 2)]
