"""

1428.
Medium



1425. Constrained Subsequence Sum
1358. Number of Substrings Containing All Three Characters
1248. Count Number of Nice Subarrays
1234. Replace the Substring for Balanced String
1004. Max Consecutive Ones III
930. Binary Subarrays With Sum
992. Subarrays with K Different Integers
904. Fruit Into Baskets
862. Shortest Subarray with Sum at Least K
239. Sliding window maximum
209. Minimum Size Subarray Sum

"""



import collections
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        maxd = collections.deque()   # between i and current, all the possible max for subarrays including current element
        mind = collections.deque()
        for a in nums:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            while maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()  # shrink the window and maintain the min and max
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums) - i


if __name__ == '__main__':

    sol = Solution()
    method = sol.longestSubarray

    cases = [
        (method, ([10,1,2,4,7,2,5],5), 5),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))