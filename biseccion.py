from typing import Callable
from result import Result, ErrorType


def bolzano(f: Callable, left_bound: float, right_bound: float) -> bool:
    """
    Aplica el teorema de Bolzano: determina si existe un 0 en cierto
    intervalo de una función.

    Nota: el recíproco del teorema de Bolzano es falso.

    Es equivalente a:
        f(left_bound) * f(right_bound) < 0
    """
    return f(left_bound) * f(right_bound) < 0


def biseccion(f: Callable, left_bound: int, right_bound: int, tol: float = 10 ** -8, iter_max: int = 1000) -> Result:
    """
    Aplica teorema de la bisección.

    f es una función Callable. Puede ser una función Lambda.
    """

    if not bolzano(f, left_bound, right_bound):
        return Result("Bisección Error: No cumple teorema de Bolzano").print_all()

    error = 0
    x = 0
    for i in range(0, iter_max + 1):
        x = (left_bound + right_bound) / 2

        if bolzano(f, x, right_bound):
            left_bound = x
        else:
            right_bound = x

        error = abs(f(x))

        if error < tol:
            return Result("Bisección", x, i, error, ErrorType.FUNCION, f, iter_max).print_all()

    return Result("Bisección Warning: Reached iter_max", x, iter_max, error, ErrorType.FUNCION, f, iter_max).print_all()

