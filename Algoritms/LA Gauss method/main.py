from Libraries.Matrixcalc import Matrix


def GaussianMethod(M: Matrix)->Matrix:
    # Forward
    for j in range(M.cols):
        for i in range(j, M.rows):
            if i == j:
                delta = M[j][j]
                if delta == 0:
                    cur_col = [x!=0 for x in M.get_column(j)]
                    try:
                        ind = cur_col.index(True)
                        M.swipe_row(0, ind)
                    except:
                        raise ValueError("Matrix error")
                    return GaussianMethod(M)
                M.mult_row(i, 1/delta)
            else:
                delta = M[i][j]
                M.set_row(
                    i,
                    [M.get_row(i)[k] - delta*M.get_row(j)[k] for k in range(M.cols)]
                )
            print(M, i, j)


M = Matrix(
    n_rows=3,
    n_cols=3,
)
print(M)
GaussianMethod(M)