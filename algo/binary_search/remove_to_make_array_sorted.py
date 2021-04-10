"""
1574.
Medium


"""


import bisect

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        # find non decreasing subarray starting at the 0
        left_ind = 0
        i = 0
        while i < n - 1:
            if arr[i] > arr[i+1]:
                break
            i += 1
        
        left_ind = i
        
        # sorted array
        if i == n - 1:
            return 0
        
        # find non increasing subarray from the end
        right_ind = n - 1
        i = n - 1
        while i >= 1:
            if arr[i] < arr[i-1]:
                right_ind = i
                break
            i -= 1

        # examine the left sorted array
        min_removed = n
        for i in range(left_ind + 1):
            j = bisect.bisect_left(arr, arr[i], right_ind)
            removed = j - i - 1
            min_removed = min(min_removed, removed)
        
        # compare to keeping the right sequence
        min_removed = min(min_removed, right_ind)
        
        return min_removed


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.findLengthOfShortestSubarray, ([1,3,7,3,2,1], ), 3),
        (sol.findLengthOfShortestSubarray, ([1,2,3,10,4,2,3,5], ), 3),
        (sol.findLengthOfShortestSubarray, ([6,3,10,11,15,20,13,3,18,12], ), 8),
        (sol.findLengthOfShortestSubarray, ([10,13,17,21,15,15,9,17,22,22,13], ), 7),
        (sol.findLengthOfShortestSubarray, ([16,10,0,3,22,1,14,7,1,12,15], ), 8),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))