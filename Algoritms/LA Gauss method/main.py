from Libraries.Matrixcalc import Matrix

def GaussMethod(A: Matrix):
    # Straight stroke
    for j in range(A.rows):
        for i in range(1, A.cols):
            cur_row = A[i]
            if A[i][j] == 0: continue
            delta = -(A[j][j]/A[i][j])
            if not(-0.000001 < delta < 0.000001): continue
            A.body[i] = list(map(lambda x:x*delta, cur_row))
    return A
M = Matrix(
    n_rows=4,
    n_cols=5,
)
print(M)
GaussMethod(M)