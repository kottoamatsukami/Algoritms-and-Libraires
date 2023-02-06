import numpy as np

X = [1, -124, 342, 43]
Y = [4, 3, -2, 4]



assert len(X) == len(Y), "X and Y must have the same length"
x_array = np.array([
    [x**j for j in range(len(X))] for x in X
])
y_array = np.array(Y)

def interpolate(solve, x):
    return sum([solve[i]*x**i for i in range(len(solve))])

solve = np.linalg.solve(x_array, y_array)
print(interpolate(solve, 3), solve)