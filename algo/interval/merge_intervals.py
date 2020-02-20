"""

56. Merge intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            
        def merge_two_intervals(i1, i2):
            if i1[0] > i2[0]:
                return merge_two_intervals(i2, i1)
            
            if i1[1] < i2[0]:
                return [i1, i2]
            else:
                return [[min(i1[0], i2[0]), max(i1[1], i2[1])]]
        
        intervals.sort()
        n = len(intervals)
        
        if n <= 1:
            return intervals
        
        ans = merge_two_intervals(intervals[0], intervals[1])
        for j in range(2, n):
            i = ans.pop(-1)
            merged = merge_two_intervals(i, intervals[j])
            ans.extend(merged)
                
        return ans
        
