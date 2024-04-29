from math import log, exp

def write_to_csv(params):
    x1, x2, x3 = params

    with open('results.csv', 'a', encoding='utf-8') as file:
        file.write(f'{x1},{x2},{x3},{f(x1,x2,x3)}\n')


def f(x1, x2, x3):
    result = (x1 ** 4) - 5 * x1 * (x2 ** 2) + -4 * (x2 ** 2) * \
        (x3 ** 2) - 10 * (x3 ** 3) + 2 * x1 - x2 + \
        exp(x3) - log(x1 ** 2 + x2 ** 2 + 1)
    return result


def minimize_f(x1, x2, x3):
    t, epsi = 0.001, 0.005
    converged = False

    while not converged:

        dx1 = -(2*x1)/(x1**2+x2**2+1)+4*(x1**3)-5*(x2**2)+2
        dx2 = -(2*x2)/((x2**2)+(x1**2)+1)-8*(x3**2)*x2-10*x1*x2-1
        dx3 = exp(x3)-30*(x3**2)-8*(x2**2)*x3

        x1 -= t*dx1
        x2 -= t*dx2
        x3 -= t*dx3

        write_to_csv([x1, x2, x3])

        converging = [abs(dx) <= epsi for dx in (dx1, dx2, dx3)]
        converged = True in converging

    return x1, x2, x3

minimize_f(1, 0, 0)




