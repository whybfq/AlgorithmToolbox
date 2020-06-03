def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n % 60):
        previous, current = current % 10, (previous + current) % 10
    return previous * current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
