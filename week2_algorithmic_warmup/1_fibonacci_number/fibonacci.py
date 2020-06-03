import sys
from math import sqrt


def calc_fib_fast(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(n + 1):
        previous, current = current, previous + current
    return current


def calc_fib(n):
    if n <= 0:
        return 0
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


def fibonacci_(n):
    a = sqrt(5)
    b = 1 / a
    return int(b * ((0.5 + a/2) ** n - (0.5 - a/2) ** n))


if __name__ == '__main__':
    n = int(sys.stdin.read())  # n = int(input())
    print(calc_fib_fast(n))
    print(fibonacci_(n))
    print(calc_fib(n))
