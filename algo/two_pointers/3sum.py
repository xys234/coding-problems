"""

15. 3Sum (Medium)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Space complexity: O(1)
Time complexity:  O(n^2)

"""


class Solution(object):

    def threeSum_two_pointer(self, nums):
        if len(nums) == 0:
            return []
        nums, i, res = sorted(nums), 0, []
        while i < len(nums) - 2 and nums[i] <= 0:
            if nums[i] != nums[i-1] or i == 0:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while k > j and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1

            i += 1
        return res

    def threeSum4(self, nums):

        n = len(nums)
        nums.sort()
        res = []
        k = n - 1
        while k >= 2:
            curr = nums[k]
            for t in self.two_sum(nums, k, -curr):
                res.append(t+[curr])
            while k >= 2 and nums[k] == curr:
                k -= 1
        return res

    def two_sum(self, nums, end_pos, target):
        """
        Find all pairs that add up to target for sub-array nums[:end_pos]
        :param end_pos:
        :param target:
        :return:
        """

        res = []
        l, r = 0, end_pos - 1
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[l], nums[r]])
                l_val = nums[l]
                while l < r and l_val == nums[l]:
                    l += 1
                r_val = nums[r]
                while l < r and r_val == nums[r]:
                    r -= 1

            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return res


if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-4, -2, -1]
    # nums = [0, 0, 0, 0]
    sol = Solution()
    method = sol.threeSum4

    cases = [
        (method, ([-1, 0, 1, 2, -1, -4],), [[-1, 0, 1], [-1, -1, 2]]),
        (method, ([0,0,0,0],), [[0,0,0]]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))