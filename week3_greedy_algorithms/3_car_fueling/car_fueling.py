'''
https://www.coursera.org/lecture/algorithmic-toolbox/car-fueling-implementation-and-analysis-shwg1

Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1, stop2, . . . , stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
Constraints. 1 ≤ 𝑑 ≤ 105. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.
# Input:
950
400
4
200 375 550 750
# Output:
# 2
# The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices
# to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill
# one would only be able to travel at most 800 miles.

Sample 2.
Input:
10
3
4
1 2 5 9
Output:
-1
One cannot reach the gas station at point 9 as the previous gas station is too far away.

Sample 3
Input:
200
250
2
100
150
Output:
0
There is no need to refill the tank as the car starts with a full tank and can travel for 250 miles
whereas the distance to the destination point is 200 miles.
Time used: 1.19/5.00, memory used: 23334912/536870912.
'''
import sys
import numpy as np
no_stops = 0  # number of stops


# have some problems   #  incorrect
def min_refills(distance, tank, stops):  # O(n) only change currentRefill changes at most linear time
    """
        :type distance: the distance from A to B
        :type tank: int  a car can travel at most tank (L) with full tank
        :type stops: int a series stop refill stations
    """
    stops.append(distance)
    n = len(stops)   # n gas stations at distances stops[0] <= stops[1] <=... stops[n]
    numRefills, currentRefill = 0, 0
    while currentRefill <= n:
        lastRefill = currentRefill
        # if stops[ currentRefill + 1 ] - stops[ lastRefill ] > tank:
        #     return -1  # impossible
        while currentRefill <= n and stops[currentRefill + 1] - stops[lastRefill] <= tank:  # and stops[currentRefill] <= distance
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1  # impossible
        if currentRefill <= n:
            numRefills += 1
        return numRefills


def compute_min_refills(distance, tank, stops):
    """
    :type distance: the distance from A to B
    :type tank: int  the farthest distance car can arrive
    :type stops: int a series stop refill stations
    """
    global no_stops
    stops.append(distance)  # should already sorted
    # stops = np.sort(stops)
    current_stop, i = 0, 0

    while current_stop < distance:
        if tank < stops[i] - current_stop:
            if stops[i-1] == current_stop:
                no_stops = -1
                break
            elif stops[i-1] > current_stop:
                current_stop = stops[i-1]
                i -= 1
                no_stops += 1
                # print(current_stop)
        if i == len(stops) - 1 and tank >= (stops[i] - current_stop):
            current_stop = stops[i]
            # print('stop here')
            break
        if i == len(stops) - 1 and tank < (stops[ i ] - current_stop):
            no_stops = -1
            break

        if i == len(stops) - 1 and tank < (stops[ i ] - current_stop):
            no_stops = -1
            break
        # print(i)
        i = i + 1

    # print(current_stop)
    return no_stops
    # if distance <= tank:
    #     return 0
    # station, back = 0, tank
    # cost, a = [], 0  # the cost between different stations
    # for i in stops:
    #     if i - a > tank:
    #         return -1
    #     cost.append(i-a)
    #     a = i
    # # print(cost)
    #
    # for i in cost:
    #     if tank > i:
    #         tank -= i
    #     elif tank <= i:
    #         station += 1
    #         tank = back
    # return station


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())  # stops is a list
    print(compute_min_refills(d, m, stops))  # correct way1
    print(min_refills(d, m, stops))  # have some problems
