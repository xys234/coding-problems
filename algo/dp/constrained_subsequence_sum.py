"""

1425.
Hard

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


2020.05.07: TLE then pass with hints
2020.05.31: 2nd attempt

"""

from typing import List
from collections import deque


class MaxWindow:
    def __init__(self, k):
        self.k = k
        self.maxd = deque()
    
    def add(self, x):
        while self.maxd and x > self.maxd[-1]:
            self.maxd.pop()
        self.maxd.append(x)
    
    def remove(self, removed):
        if removed is not None and self.maxd[0] == removed:
            self.maxd.popleft()

    def get_max(self):
        return self.maxd[0]


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        m = len(nums)
        # dp[i] max. sum of the seq. for array ending at i including element i
        dp = [-float('inf') for _ in range(m)]    
        dp[0] = nums[0]
        maxd = deque()
        maxd.append(dp[0])
        
        def max_prev_k(new, maxd, remove=None):
            
            while maxd and new > maxd[-1]:
                maxd.pop()
            maxd.append(new)
            
            if remove is not None:
                if maxd[0] == remove:
                    maxd.popleft()
            
        for i in range(1, m):
            dp[i] = nums[i] + max(0, maxd[0])
            
            # get the maximum of the previous k dp values
            if i < k:
                max_prev_k(dp[i], maxd)
            else:
                max_prev_k(dp[i], maxd, dp[i-k])

        return max(dp)

    def constrainedSubsetSum2(self, nums: List[int], k: int) -> int:
        """
        
        dp[i] is the max sum for the elements including i. 
        state transition: max(dp[i-1], dp[i-2], ... dp[i-k])
        use a sliding window to reduce the time complexity to constant time by recording the 
        max solution before dp[i]

        Time complexity: O(n), Space: O(n)
        """
        n = len(nums)
        dp = [-float('inf') for _ in range(n)]
        dp[0] = nums[0]
        
        window = MaxWindow(k+1)   # maximum k+1 elements in the window
        window.add(dp[0])
        
        for i in range(1, n):
            if i > k:
                window.remove(removed=dp[i-k-1])
            curr_max = window.get_max()
            dp[i] = max(dp[i], nums[i], curr_max+nums[i])
            window.add(dp[i])
        
        return max(dp)

if __name__ == '__main__':

    sol = Solution()
    method = sol.constrainedSubsetSum2

    cases = [
        # (method, ([10,2,-10,5,20],2), 37),
        (method, ([10,-2,-10,-5,20],2), 23),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))