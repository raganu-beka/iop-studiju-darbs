import numpy as np
from plot4d import plotter
from math import exp, log

def f(x1, x2, x3):
    result = (x1 ** 4) - 5 * x1 * (x2 ** 2) + -4 * (x2 ** 2) * \
        (x3 ** 2) - 10 * (x3 ** 3) + 2 * x1 - x2 + \
        exp(x3) - log(x1 ** 2 + x2 ** 2 + 1)
    return result


gifname = plotter.plot4d(f, np.linspace(0,1,50), func_name="f",fps=5)

