'''
Code problem: fractional knapsack

The first line. of the input contains the number 1≤n≤103 of items and
the weight 0≤W≤2⋅106 of a knapsack. The next n lines define
the cost 0≤ci≤2⋅106 and the weight 0≤ wi ≤2⋅106 of i-th item
(n, W, ci's, wi's are integers).

Output the maximal possible cost of the knapsach with
at least four digits of precision.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.0000

Description:
intput 3 items, capacity=50
and then 3 things, each value and each weight
To achieve the value 180, we take the first item and the third item into the bag.
Sample 2.
Input:
1 10
500 30
Output:
166.6667
Here, we just take one third of the only available item.

Memory Limit: 256 MB
Time Limit: 5 seconds
'''
import sys


def get_optimal_value(capacity, weights, values):  # len(weights) = len(values)
    # n = len(values)
    #
    # K = [[0 for x in range(capacity+1)] for x in range(n+1)]
    #
    # for i in range(n+1):
    #     for w in range(capacity+1):
    #         if i == 0 or w == 0:
    #             K[i][w] = 0
    #         elif weights[i-1] <= w:
    #             K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
    #         else:
    #             K[i][w] = K[i-1][w]
    # return K[n][capacity]

    totalCost, costWeight, n = 0.0, [], len(weights)

    for i in range(n):
        costWeight.append((values[i], weights[i], values[i] * 1.0/weights[i]))

    sortedWeight = sorted(costWeight, key=lambda x: x[2], reverse=True)   # descend according to the unit cost

    for i in sortedWeight:
        if capacity >= i[1]:
            capacity -= i[1]
            totalCost += i[0]
        else:
            totalCost += capacity * 1.0 / i[1] * i[0]
            break
    return totalCost


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))  # data = list(map(int, input().split())
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]  # values list
    weights = data[3:(2 * n + 2):2]  # weights list
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))  # at least 4 digits
