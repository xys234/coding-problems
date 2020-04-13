"""

442.
Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        # use remainder to get the index. add the length to mark visitation
        
        for num in nums:
            nums[(num-1)%n] += n
        
        return [i+1 for i, num in enumerate(nums) if num > 2*n]


if __name__=='__main__':

    sol = Solution()
    method = sol.findDuplicates

    cases = [

        (method, ([4,3,2,7,8,2,3,1],), [2,3]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))