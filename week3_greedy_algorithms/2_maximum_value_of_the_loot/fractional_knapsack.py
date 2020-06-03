# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    n = len(values)
    if n == 0 or capacity == 0:
        return 0
    value = 0.0
    unit = []
    for i in values:
        for j in weights:
            unit.append(i/j)
    b = unit.copy()
    b.sort(reverse=True)

    while capacity > 0:
        capacity -= weights[unit.index(b[0])]

    # return value
    pass


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print(values, weights)
    # opt_value = get_optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))  # at least 4 digits
