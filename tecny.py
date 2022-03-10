from typing import Callable


def f(x: float) -> float:
    return (x ** 2) - 2


def df(x: float):
    return 2 * x


def approx_root(x: float, f: Callable[[float], float], df: Callable[[float], float], eps=1e-8) -> float:
    oldx = x + (2 * eps)
    while abs(x - oldx) > eps:
        oldx = x
        x = x - f(x) / df(x)
    return x


x = approx_root(2.5, f, df)
print(x, x ** 2)
