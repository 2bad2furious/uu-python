from typing import Callable


def bisection(f: Callable[[float], float], a: float, b: float, eps: float = 1e-8) -> float:
    while abs(a - b) > eps:
        c = a + (b - a) * 0.5
        if f(a) * f(c) < 0:
            b = c
        elif f(c) * f(b) < 0:
            a = c
        else:
            raise Exception('bad boundaries')
    return a


print(bisection(lambda x: (x ** 2) - 2, 1, 8))
