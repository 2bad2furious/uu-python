def polynom(v, *args: int) -> int:
    result = args[0]
    for n, a in enumerate(args[1:]):
        result += a ** (n + 1)

    return result


if __name__ == '__main__':
    print(polynom(1, 3, 2, 1))
