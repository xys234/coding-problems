"""

992.
hard

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length


2020.05.08: 
Use slinding window to solve subarraysWithAtMostKDistinct
When more than K distinct exist, shrink the window from left
For each valid window ending at j, all its subarray ending at j also valid
Even though all subarrays within the window valid, we cannot include
them due to potential double counting as iterating windowEnd to the right

scheme: Fix right end and shrink left

"""

from typing import List

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        class Window:
            def __init__(self):
                self.nunique = 0
                self.counter = {}
            
            def add(self, x):
                if x in self.counter:
                    self.counter[x] += 1
                else:
                    self.counter[x] = 1
                    self.nunique += 1
            
            def remove(self, x):
                if x in self.counter:
                    self.counter[x] -= 1
                    if self.counter[x] == 0:
                        self.counter.pop(x)
                        self.nunique -= 1
                else:
                    raise ValueError(f"{x} not exists in the window")

        def subarraysWithAtMostKDistinct(nums, k):
            r = 0
            w = Window()
            n = len(nums)
            l = 0
            num_arrays = 0

            while r < n:
                w.add(nums[r])

                while l <= r and w.nunique > k:
                    w.remove(nums[l])
                    l += 1
                
                num_arrays += r - l + 1
                r += 1

            return num_arrays


        a1 = subarraysWithAtMostKDistinct(A, K)
        a2 = subarraysWithAtMostKDistinct(A, K-1)
                
        return a1 - a2

if __name__ == '__main__':

    sol = Solution()
    method = sol.subarraysWithKDistinct

    cases = [
        (method, ([1,2,1,2,3],2), 7),
        (method, ([1,2,1,3,4],3), 3),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))