"""
Input format. Integer n.
Output format. In the first line, output the maximum number k such that
n can be represented as the sum of k pairwise distinct positive integers.
In the second line, output k pairwise distinct positive integers that sum up to n
(if there are many such representations, output any of them).

Constraints. 1 ≤ n ≤ 109. Sample 1.

Input:
6
Output:
3
1 2 3
76
Sample 2.
Input:
8
Output:
3
1 2 5
Sample 3.
Input:
2
Output:
1
2
"""

import sys


def optimal_summands(n):
    summands = [ ]
    # write your code here
    return summands


if __name__ == '__main__':
    n = int(sys.stdin.read())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
