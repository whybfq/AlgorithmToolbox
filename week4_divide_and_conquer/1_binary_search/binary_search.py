# Page 84
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if x > a[mid]:
            left = mid + 1  # binary_search(a[left+1: right], x)
        elif x < a[mid]:
            right = mid - 1  # binary_search(a[left, mid-1], x)
        else:
            return mid    
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[ i ] == x:
            return i
    return -1


if __name__ == '__main__':
    seq = [int(i) for i in input().split()]
    search_seq = [int(i) for i in input().split()]
    n = seq[0]
    seq = seq[1:]
    
    soln = list()
    for i in search_seq[1:]:
        ans = binary_search(seq, i)
        soln.append(ans)
    print(' '.join([str(i) for i in soln]))
