"""
Advanced code problem: pairwise different summands

Given an integer 1≤n≤109 find the maximal number k such that n can be represented as a sum of pairwise different positive integers. In the first line output k, in the next line output k summands.

Sample Input 1:
4
Sample Output 1:
2
1 3

Sample Input 2:
6
Sample Output 2:
3
1 2 3

Memory Limit: 256 MB
Time Limit: 5 seconds
'''
n = int(input())

total = 0
increment = 1
count = 0
listOfNum = []

while total + increment <= n:
    total += increment
    listOfNum.append(increment)
    increment += 1
    count += 1

listOfNum[count-1] += n - total

print(count)
print(*listOfNum)


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

Memory Limit: 256 MB
Time Limit: 5 seconds

"""

import sys


def optimal_summands(n):
    total, increment, count, listOfNum = 0, 1, 0, []

    while total + increment <= n:
        total += increment
        listOfNum.append(increment)
        increment += 1
        count += 1
    listOfNum[count - 1] += n - total
    return listOfNum


if __name__ == '__main__':
    summands = optimal_summands(int(sys.stdin.read()))
    print(len(summands))  # count = len(summands)
    for x in summands:
        print(x, end=' ')
