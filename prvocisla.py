from typing import Iterable


def prvocisla() -> Iterable[int]:
    primes = set(())
    i = 2
    while True:
        if not any(filter(lambda prime: i % prime == 0, primes)):
            primes.add(i)
            yield i

        i = i + 1


def print_prvocisla_until(limit: int) -> None:
    for i in prvocisla():
        if i > limit:
            break
        print(i)


def print_n_prvocisel(n: int) -> None:
    for i in prvocisla():
        if n == 0:
            break
        n = n - 1
        print(i)
