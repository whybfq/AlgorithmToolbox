
""" Page 85
Prove that this idea leads to an algorithm with running
time O(n log n).
Input format. The first line contains an integer n, the next one contains
Chapter 6. Divide-and-Conquer
a sequence of n non-negative integers a1, . . . , an.
Output format. Output 1 if the sequence contains an element that ap-
pears more than n/ 2 times, and 0 otherwise.
Constraints. 1 ≤ n ≤ 105; 0 ≤ ai ≤ 109 for all 1 ≤ i ≤ n. Sample 1.
Input:
5
2 3 9 2 2
Output:
1

2 is the majority element.

Sample 2.
Input:
4
1 2 3 1
Output:
0
This sequence does not have a majority element (note that the element 1 is not a majority element).

"""
import sys


def get_majority_element(seq, l, r):
    if l + 1 == r or l + 2 == r:
        return seq[ l ]
    m = (l + r) // 2
    left = get_majority_element(seq, l, m)
    right = get_majority_element(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[ l:r ]:
        if i == left:
            c1 += 1
        elif i == right:
            c2 += 1
    if c1 > (r - l) // 2 and left != -1:
        return left
    elif c2 > (r - l) // 2 and right != -1:
        return right
    else:
        return -1


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    print(int(get_majority_element(a, 0, n) != -1))
