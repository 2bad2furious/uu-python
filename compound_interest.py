import math
from typing import Iterable


def compound_interest_monthly(deposit: float, interest_pa: float) -> Iterable[int]:
    deposit_int = int(round(deposit * 100))

    interest_pm_int = math.pow(1 + (interest_pa / 100), 1 / 12)

    state = deposit_int
    yield state

    while True:
        state = round(state * interest_pm_int)
        yield state

        state = state + deposit_int


def compound_interest_pa(deposit: float, interest_pa: float) -> Iterable[int]:
    withIndex: Iterable[int, int] = enumerate(compound_interest_monthly(deposit, interest_pa))
    filtered = filter(lambda v: v[0] % 12 == 0, withIndex)
    return map(lambda v: v[1], filtered)


def number_of_years_until_total(deposit: float, interest_pa: float, total: float) -> int:
    total_int = int(round(total * 100))
    for year, value in enumerate(compound_interest_pa(deposit, interest_pa)):
        if value >= total_int:
            return year

    raise Exception('finite compound calculation')


def total_after_years(deposit: float, interest_pa: float, years: int) -> int:
    interest_iterator = compound_interest_pa(deposit, interest_pa)
    for year, value in enumerate(interest_iterator):
        if year >= years:
            return value

    raise Exception('finite compound calculation')


def total_after_n_months(deposit: float, interest_pa: float, n_months: int) -> float:
    q = math.pow(1 + (interest_pa / 100), 1 / 12)
    return deposit * q * ((math.pow(q, n_months) - 1) / (q - 1))


print(total_after_years(1000.0, 2.39, 1))
print(total_after_n_months(1000.0, 2.39, 12))

print("m in", number_of_years_until_total(1000.0, 2.39, 1000_000))
print("amount in 47", total_after_n_months(1000.0, 2.39, 47 * 12))
