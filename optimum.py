from math import log, exp
from scipy.optimize import minimize

def f(params):
    x1, x2, x3 = params

    result = (x1 ** 4) - 5 * x1 * (x2 ** 2) + -4 * (x2 ** 2) * \
        (x3 ** 2) - 10 * (x3 ** 3) + 2 * x1 - x2 + \
        exp(x3) - log(x1 ** 2 + x2 ** 2 + 1)
    return result


res = minimize(f, x0=[1, 0, 0], method='CG')
print(res)

print(f([0, 0, 0]))

# -0.9096429154461436