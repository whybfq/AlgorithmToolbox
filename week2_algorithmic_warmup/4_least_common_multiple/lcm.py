# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm(a, b):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    a, b = map(int, sys.stdin.read().split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))
