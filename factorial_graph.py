from math import factorial as math_factorial
from typing import Callable, Any

import numpy as np
from matplotlib.pyplot import plot, show, legend

from factorial import factorial
from measure_time import measure_time

n_values = list(range(21))  # 0 until 20


def create_data(factorial_calculation: Callable[[int], Any]) -> list[float]:
    return list(map(lambda n: measure_time(lambda: factorial_calculation(n), 100_000), n_values))


plot(n_values, create_data(factorial), label="my implementation")
plot(n_values, create_data(math_factorial), label="math.factorial")
plot(n_values, create_data(np.math.factorial), label="numpy.math.factorial")

legend()
show()
