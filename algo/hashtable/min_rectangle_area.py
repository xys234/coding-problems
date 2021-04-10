"""

LC. 939
Medium


Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.


"""

from typing import List
from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        columns = defaultdict(list)
        
        for x, y in points:
            columns[x].append(y)
        
        min_area = float('inf')
        closest_sides = {}
        for x, ps in columns.items():
            for j, y in enumerate(sorted(ps)):
                for i in range(j):
                    if (ps[i], y) in closest_sides:
                        closest_x = closest_sides[ps[i], y]
                        min_area = min(min_area, (x - closest_x) * (y - ps[i]))
                    closest_sides[ps[i], y] = x
        return min_area if min_area != float('inf') else 0