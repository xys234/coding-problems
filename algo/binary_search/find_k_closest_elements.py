"""

658
Medium

Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

Tags:
binary_search (find the first element larger than or equal to)
two pointers

"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # special cases
        if arr[0] >= x:
            return arr[:k]
        
        if arr[-1] <= x:
            return arr[-k:]
        
        # find the first element larger than or equal to x
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        pos = l
        
        # Find the right sublist with two pointers
        low, high = max(0, pos - k), min(len(arr)-1, pos + k)
        while high - low + 1 != k:
            if abs(arr[low]-x) <= abs(arr[high]-x):
                high -= 1
            else:
                low += 1
        return arr[low:high+1]
        
        
            
        
        
        
        
        