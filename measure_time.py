from time import process_time_ns
from typing import Callable, Any


def measure_time(fun: Callable[[], Any], num_of_executions: int = 1) -> float:
    if num_of_executions < 0:
        raise Exception('num of executions should be a positive number, ' + str(num_of_executions) + ' received')

    start = process_time_ns()

    for _ in range(num_of_executions):
        fun()

    end = process_time_ns()
    return end - start
