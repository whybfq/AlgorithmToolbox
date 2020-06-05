# Input format. The first line contains an integer n, the second one contains a sequence of integers
# price1, . . . , pricen, the third one contains a sequence of integers clicks1, . . . , clicksn.
# Output format. Output the maximum value of (price1 · c1 + · · · + pricen · cn),
# where c1, . . . , cn is a permutation of clicks1, . . . , clicksn.
# Constraints. 1 ≤ n ≤ 103; 0 ≤ pricei , clicksi ≤ 105 for all 1 ≤ i ≤ n.

'''

Sample 1.
Input:
1
23
39
Output:
897
897 = 23 · 39.
Sample 2.
Input:
3
2 3 9
7 4 2
Output:
79
79 = 7 · 9 + 2 · 2 + 3 · 4.

'''

import sys


def max_dot_product(a, b):
    # write your code here
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[ i ] * b[ i ]
    return res


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[ 0 ]
    a = data[ 1:(n + 1) ]
    b = data[ (n + 1): ]
    print(max_dot_product(a, b))
