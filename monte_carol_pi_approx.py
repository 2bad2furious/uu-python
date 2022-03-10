from random import random


def in_circle(x, y):
    return (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.5 ** 2


N = 100_000_000

if __name__ == '__main__':
    print((4 * sum(map(lambda _: in_circle(random(), random()), range(N)))) / N)
