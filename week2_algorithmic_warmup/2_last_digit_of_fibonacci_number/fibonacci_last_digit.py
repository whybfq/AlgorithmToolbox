# Uses python3
import sys
from math import sqrt


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(n % 60):
        previous, current = current % 10, (previous % 10 + current % 10) % 10
    return current % 10


def fibonacci_(n):
    a = sqrt(5)
    b = 1 / a
    return int(b * ((0.5 + a/2) ** n - (0.5 - a/2) ** n))


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_fibonacci_last_digit_naive(n))
    print(fibonacci_(n))
