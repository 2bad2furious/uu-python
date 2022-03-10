from __future__ import annotations

from math import sqrt
from typing import Union, Callable, Tuple


class Complex:

    def __hash__(self) -> int:
        pass

    def __init__(self, real: float, imaginary: float):
        self.__real = real
        self.__imaginary = imaginary
        pass

    def __add__(self, other: Union[float, Complex]) -> Complex:
        return self.__compute(other, lambda a, b, c, d: (a + c, b + d))

    def __sub__(self, other: Union[float, Complex]) -> Complex:
        return self.__compute(other, lambda a, b, c, d: (a - c, b - d))

    def __mul__(self, other: Union[float, Complex]) -> Complex:
        return self.__compute(other, lambda a, b, c, d: (a * c - b * d, a * d + b * c))

    def __floordiv__(self, other: Union[float, Complex]) -> Complex:
        return self.__compute(other, self.__computeDiv)

    def __computeDiv(self, a: float, b: float, c: float, d: float) -> Tuple[float, float]:
        denominator = c ** 2 + d ** 2

        return (a * c + b * d) / denominator, (b * c - a * d) / denominator

    def conj(self) -> Complex:
        return Complex(self.__real, self.__imaginary * -1.0)

    def __abs__(self) -> float:
        return sqrt(self.__real ** 2 + self.__imaginary ** 2)

    def __compute(
            self,
            other: Union[float, Complex],
            complex_calc: Callable[[float, float, float, float], Tuple[float, float]]
    ) -> Complex:
        if isinstance(other, Complex):
            return Complex(*complex_calc(self.__real, self.__imaginary, other.__real, other.__imaginary))

        if isinstance(other, float) or isinstance(other, int):
            return Complex(*complex_calc(self.__real, self.__imaginary, other, 0))

        raise NotImplementedError(f"Unsupported type {type(other)}")

    def __str__(self):
        return f"({self.__real} {'+' if self.__imaginary > 0 else '-'} {abs(self.__imaginary)}i)"


c = Complex(1, 2)
print(c)
c += 2
print(c)
