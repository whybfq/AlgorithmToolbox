"""
Page 73

Input format. The first line of the input contains the number n of segments.
Each of the following n lines contains two integers ai and bi (separated by a space)
defining the coordinates of endpoints of the i-th segment.

Output format. The minimum number m of points on the first line and the integer
coordinates of m points (separated by spaces) on the sec- ond line. You can output the points in any order.
If there are many such sets of points, you can output any set.

Constraints. 1 ≤ n ≤ 100; 0 ≤ ai ≤ bi ≤ 109 for all i .

Sample 1.
Input:
3
1 3
2 5
3 6
Output:
1
3
All three segments [1, 3], [2, 5], [3, 6] contain the point with coordinate 3.
Sample 2.
Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6

"""

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
# print(f'Segment: {Segment}')


def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    # print(f'segments is: {segments}')
    current = segments[0].end
    points.append(current)
    for s in segments:
        if (current < s.start) or (current > s.end):
            current = s.end
            points.append(current)
        # points.append(s.start)
        # points.append(s.end)
    return points


if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: Segment(x[ 0 ], x[ 1 ]), zip(data[ ::2 ], data[ 1::2 ])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)  # for p in points: print(p, end=' ')
