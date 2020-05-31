"""

1248.
Medium

Given an array of integers nums and an integer k. 
A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5


"""

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = cnt = 0
        n = len(nums)

        while r < n:
            if nums[r] % 2 == 1:
                k -= 1
                cnt = 0
            
            while k == 0:
                cnt += 1
                if nums[l] % 2 == 1:
                    k += 1
                l += 1
            
            # same cnt until right-end hits next odd elem
            # because an even elem is added on the right end
            # it does not change the number of valid subarrays
            res += cnt
            r += 1
        return res

if __name__ == '__main__':

    sol = Solution()
    method = sol.numberOfSubarrays

    cases = [
        # (method, ([2,2,2,1,2,2,1,2,2,2],2), 16),
        (method, ([1,1,2,1,1],3), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))