import random
import math


# Globals

MAX_RAND =  5
MIN_RAND = -5


class Matrix:
    def __init__(self, n_rows: int, n_cols: int, body=None) -> None:
        self.rows = n_rows
        self.cols = n_cols
        self.body = [[None for _ in range(n_cols)] for _ in range(n_rows)]
        if body is None:
            self.__init_with_random()


    def set_row(self, i: int, new_row: list):
        if isinstance(new_row, list):
            assert len(new_row) == self.cols, "Length of new row must be equal to number of columns"
            self.body[i] = new_row
        else:
            raise TypeError(f"Expected list, got {type(new_row)}")

    def set_column(self, i: int, new_column: list):
        if isinstance(new_column, list):
            assert len(new_column) == self.rows, "Length of new column must be equal to number of rows"
            for j in range(self.rows):
                self.body[j][i] = new_column[j]
        else:
            raise TypeError(f"Expected list, got {type(new_column)}")

    def swipe_row(self, i: int, j: int):
        temp = self.body[i]
        self.set_row(i, self.body[j])
        self.set_row(j, temp)

    def swipe_column(self, i: int, j: int):
        temp = self.get_column(i)
        self.set_column(i, self.get_column(j))
        self.set_column(j, temp)

    def get_row(self, i: int):
        return self.body[i]

    def get_column(self, i: int):
        out = []
        for j in range(self.rows):
            out.append(self.body[j][i])
        return out


    def __init_with_random(self):
        for cur_row in range(self.rows):
            for cur_col in range(self.cols):
                self.body[cur_row][cur_col] = random.randint(MIN_RAND, MAX_RAND)

    def __repr__(self) -> str:
        out = "Matrix:\n"
        n = float("-inf")
        for cur_row in range(self.rows):
            for cur_col in range(self.cols):
                n = max(
                    n,
                    len(str(self.body[cur_row][cur_col])),
                )

        for cur_row in range(self.rows):
            for cur_col in range(self.cols):
                out += str(self.body[cur_row][cur_col]).rjust(n, " ") + " "
            out += "\n"
        return out

    def __getitem__(self, i: int) -> list:
        return self.body[i]

    def __mul__(self, other):
        if isinstance(other, (Matrix, Vector)):
            assert (self.cols == other.rows)
            new = Matrix(self.rows, other.cols)
            for ind_x in range(self.rows):
                for ind_y in range(other.cols):
                    cur_row = self.body[ind_x]
                    cur_col = [x[ind_y] for x in other.body]
                    new[ind_x][ind_y] = sum([cur_row[i] + cur_col[i] for i in range(self.cols)])
            return new

        elif isinstance(other, (int, float)):
            new = Matrix(self.rows, self.cols)
            for ind_x in range(self.rows):
                for ind_y in range(self.cols):
                    new[ind_x][ind_y] = self.body[ind_x][ind_y] * other
            return new

    def __add__(self, other):
        if isinstance(other, (Matrix, Vector)):
            assert (self.cols == other.cols and self.rows == other.cols)
            new = Matrix(self.rows, self.cols)
            for ind_x in range(self.rows):
                for ind_y in range(self.cols):
                    new[ind_x][ind_y] = self.body[ind_x][ind_y] + other.body[ind_x][ind_y]
            return new

    def __sub__(self, other):
        if isinstance(other, (Matrix, Vector)):
            assert (self.cols == other.cols and self.rows == other.cols)
            new = Matrix(self.rows, self.cols)
            for ind_x in range(self.rows):
                for ind_y in range(self.cols):
                    new[ind_x][ind_y] = self.body[ind_x][ind_y] - other.body[ind_x][ind_y]
            return new