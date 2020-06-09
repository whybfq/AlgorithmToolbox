# Uses python3
import sys
import time
import random


# def quicksort(a, l, r):
#     # print('Splitting:', a[l:r])
#     if l + 1 >= 4:
#         return
#     # pivot selection; return a random integer N ( [l, r] )
#     m = random.randint(l, r-1)
#     # temp = sorted([(0, a[0]),( (l+r)//2,a[(l+r)//2]), (-1,a[-1]), key = lambda x: x[1])
#     # m = temp[1][0]
#     a[l], a[m] = a[m], a[l]
#
#     # partition procedure
#     m1, m2 = partition3(a, l, r)
#
#     quicksort(a, l, m1)
#     quicksort(a, m2+1, r)


def partition3(a, l, r):
    pivot_value = a[l]
    p_l = i = l
    p_e = r
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1

    return [p_l, p_e]


def partition2(a, l, r):
    pivot = random.randint(l, r)
    a[r], a[pivot] = a[pivot], a[r]
    pivot_value = a[r]
    pIndex = l
    for i in range(l, r):
        if a[i] <= pivot_value:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[r], a[pIndex] = a[pIndex], a[r]
    return pIndex


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    pivot = random.randint(l, r)
    a[ l ], a[ pivot ] = a[ pivot ], a[ l ]
    pIndex = partition3(a, l, r)
    randomized_quick_sort(a, l, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, r)


# def create_array(size):
#     return [random.choice(list(range(10))) for _ in range(size)]


if __name__ == '__main__':
    # t1 = time.time()
    n, *a = list(map(int, sys.stdin.read().split()))
    # print(f'n is {n}, array: {a}')
    randomized_quick_sort(a, 0, n - 1)
    # quicksort(a, 0, n-1)
    # t2 = time.time()
    for x in a:
        print(x, end=' ')
    # print(f"time takes: {t2-t1}")
