# Page 77

"""
A sample greedy algorithm
LargestConcatenate(Numbers):
yourSalary ← empty string
while Numbers is not empty:
    maxNumber ← -∞
    for each number in Numbers:
        if number ≥ maxNumber:
            maxNumber ← number
    append maxNumber to yourSalary
    remove maxNumber from Numbers
return yourSalary

Unfortunately, this algorithm does not always maximize your salary! For example,
for an input consisting of two integers 23 and 3 it returns 233, while the largest number is 323.
while the algorithm works correctly for the case of single-digit numbers.

improve:
change if number ≥ maxNumber: to if IsBetter(number, maxNumber):

Input format. The first line of the input contains an integer n. The second line contains integers a1, . . . , an.
Output format. The largest number that can be composed out of a1, . . . , an. Constraints. 1 ≤ n ≤ 100; 1 ≤ ai ≤ 103 for all 1 ≤ i ≤ n. Sample 1.
Input:
2
21 2
Output:
221
Note that in this case the above algorithm also returns an incorrect answer 212.
Sample 2.
Input:
5
9 4 6 1 9
Output:
99641
The input consists of single-digit numbers only, so the algorithm above returns the correct answer.
Sample 3.
Input:
3
23 39 92
Output:
923923
The (incorrect) LargestNumber algorithm nevertheless produces the correct answer in this case,
another reminder to always prove the correctness of your greedy algorithms!

"""

import sys


def IsBetter(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(a: list):  # a is the numbers
    yourSalary = []
    while a:  # a != []
        maxNumber = -1
        for x in a:
            # if int(x) >= maxNumber:
            if IsBetter(x, maxNumber):
                maxNumber = x
        yourSalary.append(maxNumber)
        a.remove(maxNumber)
    return yourSalary


if __name__ == '__main__':
    # data = sys.stdin.read().split()
    # a = data[ 1: ]
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(largest_number(lst))
