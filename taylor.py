import math
from result import Result, ErrorType


def exp_taylor(x: float, tol: float = 10 ** -5, iter_max: int = 1000) -> Result:
    """
    Exponencial utilizando serie de Taylor.

    Es equivalente a:
        exp(x)
    """
    suma = 0
    error = 0
    for i in range(0, iter_max + 1):
        sumak = suma + (x ** i)/math.factorial(i)
        error = abs(sumak - suma)/abs(sumak)
        suma = sumak
        if error < tol:
            return Result("Exponencial de Taylor", suma, i, error, ErrorType.RELATIVO, x, iter_max).print_all()

    return Result("Exponencial de Taylor Warning: reached iter_max", suma, iter_max, error, ErrorType.RELATIVO,
                  x, iter_max).print_all()

