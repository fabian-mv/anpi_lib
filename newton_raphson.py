from result import Result, ErrorType
from sympy import Symbol, diff, lambdify, sympify
from biseccion import bolzano
from typing import Callable


def newton_raphson(f: str, var: Symbol, start: float, tol: float = 10 ** -8, iter_max: int = 1000) -> Result:
    """
    Aplica método de newton raphson.

    Ejemplo de f que sirve:
        f = "exp(x) - 2*x - 10"
    """
    f = sympify(f)

    dfdx = lambdify(var, diff(f, var))
    f = lambdify(var, f)

    if dfdx(start) == 0:
        return Result("Newton Raphson Error: dfdx(start) = 0").print_all()

    xk = start
    error = 0
    for i in range(0, iter_max):
        denominator = dfdx(xk)
        error = abs(f(xk))

        if abs(denominator) < 10**-15:
            return Result("Newton Raphson Warning: Stopped due to division approaching zero.", xk, i, error,
                          ErrorType.FUNCION, f, iter_max).print_all()

        xk = xk - f(xk)/denominator

        if error < tol:
            return Result("Newton Raphson", xk, i, error, ErrorType.FUNCION, f, iter_max).print_all()

    return Result("Newton Raphson Warning: Reached iter_max", xk, iter_max, error, ErrorType.FUNCION,
                  f, iter_max).print_all()


def nr_secante(f: str, var: Symbol, x0: float, x1: float, tol: float = 10 ** -8, iter_max: int = 1000) -> Result:
    """
    Aplica método de newton raphson utilizando la definición de la derivada para derivar.
    Utiliza el método de la secante para obtener la derivada.

    Ejemplo de f que sirve:
        f = "exp(x) - 2*x - 10"
    """
    f = sympify(f)
    f = lambdify(var, f)

    xk = x1
    xk_prev = x0
    error = 0
    for i in range(0, iter_max):
        denominator = f(xk) - f(xk_prev)
        error = abs(f(xk))

        if abs(denominator) < 10**-15:
            return Result("NR con secante Warning: Stopped due to division approaching zero.", xk, i, error,
                          ErrorType.FUNCION, f, iter_max).print_all()

        xk = xk - ((xk - xk_prev)*f(xk))/denominator

        if error < tol:
            return Result("NR con secante", xk, i, error, ErrorType.FUNCION, f, iter_max).print_all()

    return Result("NR con secante Warning: Reached iter_max", xk, iter_max, error, ErrorType.FUNCION,
                  f, iter_max).print_all()


def falsa_posicion(f: str, var: Symbol, left_bound: float, right_bound: float, tol: float = 10 ** -16,
                   iter_max: int = 1000) -> Result:
    """
    Aplica teorema de la falsa posición. Esto es una combinación entre el método de la bisección y la secante

    Ejemplo de f que sirve:
        f = "cos(x) - x"
    """

    f = lambdify(var, sympify(f))

    if not bolzano(f, left_bound, right_bound):
        return Result("Bisección Error: No cumple teorema de Bolzano").print_all()

    denominator = f(right_bound) - f(left_bound)
    xk = right_bound - ((right_bound - left_bound)*f(right_bound))/denominator

    if abs(denominator) < 10 ** -15:
        return Result("Falsa Posición Error: Division approaching zero.").print_all()

    error = 0
    for i in range(2, iter_max):

        if bolzano(f, xk, left_bound):
            d = f(xk) - f(left_bound)
            xk = xk - ((xk - left_bound)*f(xk))/d
            right_bound = xk

        else:
            d = f(xk) - f(right_bound)
            xk = xk - ((xk - right_bound) * f(xk))/d
            left_bound = xk

        xk = xk.evalf()

        error = abs(f(xk))

        if abs(d) < 10**-15:
            return Result("Falsa Posición Warning: Stopped due to division approaching zero.", xk, i, error,
                          ErrorType.FUNCION, f, iter_max).print_all()

        if error < tol:
            return Result("Falsa Posición", xk, i, error, ErrorType.FUNCION, f, iter_max).print_all()

    return Result("Falsa Posición Warning: Reached iter_max", xk, iter_max, error, ErrorType.FUNCION,
                  f, iter_max).print_all()


def punto_fijo(f: str, fvar: Symbol, g: str, gvar: Symbol, x0: float, tol: float = 10 ** -8, iter_max: int = 1000) -> Result:
    """
    Asume que g(x) cumple la existencia y unicidad del punto fijo.

    ejemplo:
        f = "exp(x) - 2*x - 1"
        g = "ln(2*y + 1) - y"
        punto_fijo(f, x, g, y, 1)
    """

    g = lambdify(gvar, sympify(g))
    f = lambdify(fvar, sympify(f))
    xk = x0
    error = 0
    for i in range(0, iter_max):
        xk = g(xk)

        error = abs(f(xk))
        if error < tol:
            return Result("Punto fijo", xk, i, error, ErrorType.FUNCION, f, iter_max).print_all()

    return Result("Punto fijo Warning: Reached iter_max", xk, iter_max, error, ErrorType.FUNCION,
                  f, iter_max).print_all()




















