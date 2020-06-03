import sys
import random
import numpy as np
from math import sqrt


def calc_fib_fast(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(n - 1):  # for _ in range(1, n)
        previous, current = current, previous + current
    return current


def calc_fib(n):
    # if n <= 0:
    #     return 0
    return n if n <= 1 else calc_fib(n - 1) + calc_fib(n - 2)


def fibonacci_(n):  # according to the formula
    a = sqrt(5)
    b = 1 / a
    return int(b * ((0.5 + a/2) ** n - (0.5 - a/2) ** n))


def StressTest(M):
    while True:  # 2. INFINITE LOOP
        number = random.randint(1, M)  # 3. RANDOM TEST GENERATOR
        print(f'numbers is {number}')

        result1 = calc_fib_fast(number)  # 4. > 2 WAYS
        result2 = fibonacci_(number)
        result3 = calc_fib(number)
        if result1 == result2 == result3:
            print("Ok")
        else:
            print("Wrong answer in : ", result1, result2, result3)
            break


if __name__ == '__main__':
    # n = int(sys.stdin.read())  # n = int(input())
    # print(calc_fib_fast(n))
    # print(fibonacci_(n))
    # print(calc_fib(n))
    StressTest(10)  # if number very large, it will be very slow
