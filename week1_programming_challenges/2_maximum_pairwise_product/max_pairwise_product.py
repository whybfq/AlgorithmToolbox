import random
import numpy as np


def max_pairwise_faster(numbers):
    numbers.sort()  # nlog(n)
    n = len(numbers)
    return numbers[ 0 ] if n == 1 else numbers[ n - 1 ] * numbers[ n - 2 ]


def max_pairwise_fast(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[ 0 ]
    index1 = 0
    for i in range(1, n):
        if numbers[ i ] > numbers[ index1 ]:
            index1 = i

    index2 = 1 if index1 == 0 else 0
    for second in range(1, n):
        if second != index1 and numbers[ second ] > numbers[ index2 ]:
            index2 = second

    return numbers[ index1 ] * numbers[ index2 ]


def max_pairwise_product(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[ 0 ]
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[ first ] * numbers[ second ])

    return max_product


def StreeTest(N, M):
    while True:  # 2. INFINITE LOOP
        n = random.randint(1, N)  # 3. RANDOM TEST GENERATOR
        print(f'n is {n}')
        numbers = np.random.randint(low=0, high=M, size=n)
        print(numbers)

        result1 = max_pairwise_fast(numbers)  # 4. > 2 WAYS
        result2 = max_pairwise_product(numbers)
        if result1 == result2:
            print("Ok")
        else:
            print("Wrong answer in : ", result1, result2)
            break


if __name__ == '__main__':
    StreeTest(10, 1000)
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    # print(max_pairwise_fast(input_numbers))
