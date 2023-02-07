import numpy as np
import math

PI = 3.1415926535
H = 17

def xrange(start, stop, step: float):
    if start > stop:
        return xrange(stop, start, step)
    if step == 0:
        return xrange(start, stop, 1e-1)
    if step < 0:
        return xrange(start, stop, -step)
    else:
        out = start - step
        while out < stop:
            out += step
            yield out

def f(x):
    x %= 2*3.141592
    return math.tan(x)



graph = {
    x: f(x) for x in xrange(-2, 2, 0.2)
}

X = np.array(list(graph.keys()))
Y = np.array(list(graph.values()))

assert len(X) == len(Y), "X and Y must have the same length"
x_array = np.array([
    [x**j for j in range(len(X))] for x in X
])
y_array = np.array(Y)

def interpolate(solve, x):
    return sum([solve[i]*x**i for i in range(len(solve))])


def to_desmos_form(solve):
    out = ''
    for i, coef in enumerate(map(str, solve)):
        coef = coef.replace('e-', '*10^{-')
        coef = coef.replace('e+', '*10^{+')
        if '{' in coef: coef += '}'
        coef += '*x^{' + str(i) + '}'
        out += coef + ' '
    return out.strip().replace(' ', '+')

solve = np.linalg.solve(x_array, y_array)

import matplotlib.pyplot as plt
with open("func.txt", "w") as f:
    f.write(to_desmos_form(solve))


interpol = [interpolate(solve, x) for x in graph.keys()]

plt.plot(graph.keys(), graph.values(), label='Оригинал')
plt.plot(graph.keys(), interpol, label='Интерполированный чурбан')
plt.legend()
plt.show()
print("Ошибка:", sum([(interpol[i] - list(graph.values())[i])**2 for i in range(len(graph.keys()))]))