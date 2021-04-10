"""

LC.1060


Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

"""

from typing import List


class Solution: 
    
    def first_missing(self, A: List[int], K:int) -> int:
        n = len(A)
        missing_count = A[-1] - A[0] + 1 - n  
        if missing_count < K:
            return A[-1] + K - missing_count
        
        l, r = 0 , n-1
        while l < r:
            mid = l + (r - l) // 2
            if self.get_missing_count(A, mid) < K:
                l = mid + 1
            else:
                r = mid
        return A[l-1] + K - self.get_missing_count(A, l-1)
    

    def get_missing_count(self, nums, mid):
        return nums[mid] - nums[0] - mid




if __name__ == "__main__":
    sol = Solution()
    method = sol.first_missing

    cases = [
        # (method, ([4,7,9,10], 1), 5),
        (method, ([4,7,9,10], 3), 8),
        # (method, ([1,2,4], 3), 6),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))