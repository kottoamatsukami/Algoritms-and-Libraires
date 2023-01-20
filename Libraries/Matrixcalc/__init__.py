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
                out += str(self.body[cur_row][cur_col]).center(n, " ") + " "
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


class Vector(Matrix):
    def __init__(self, vertical: bool, n: int, body=None):
        self.vertical = vertical
        if self.vertical:
            super().__init__(n_rows=n, n_cols=1, body=body)
        else:
            super().__init__(n_rows=1, n_cols=n, body=body)

class LinearTransformation(Matrix):
    def __init__(self, n_rows: int, n_cols: int, body=None):
        super().__init__(n_rows=n_rows, n_cols=n_cols, body=body)


class RotateMatrixR2(LinearTransformation):
    def __init__(self):
        super().__init__(n_rows=2, n_cols=2, body=[[None, None], [None, None]])

    def init_angle(self, alpha: float):
        alpha = math.radians(alpha)
        print(alpha)
        self.body = [
            [math.cos(alpha), -math.sin(alpha)],
            [math.sin(alpha), math.cos(alpha)],
        ]

    def transform(self, v: Vector, alpha=None):
        if alpha is not None:
            self.init_angle(alpha)
        return self*v


test_vector = Vector(True, 2)
print(test_vector)
rot_matrix = RotateMatrixR2()
rot_matrix.init_angle(180)
print(rot_matrix.transform(test_vector))