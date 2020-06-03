# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, sys.stdin.read().split())
    # print(gcd_naive(a, b))
    print(gcd(a, b))
