def polynom(v, *args: int) -> int:
    result = 0
    for n, a in enumerate(args):
        result += a * (v ** n)

    return result


if __name__ == '__main__':
    print(polynom(2, 3, 2, 1))  # 3 + 2(2) + 1(2 * 2)
