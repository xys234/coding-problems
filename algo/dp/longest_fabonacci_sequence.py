"""

873. Length of Longest Fibonacci Subsequence
Medium

1st: 2020-08-30

"""


from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        inds = {x:i for i, x in enumerate(A)}
        dp = defaultdict(lambda: 2)
        ans = 0
        
        for i, num in enumerate(A):
            for j in range(i):
                prev_elem_ind = inds.get(num - A[j], -1)
                if prev_elem_ind >= 0 and prev_elem_ind < j:
                    dp[(i, j)] = dp[(j, prev_elem_ind)] + 1
                    ans = max(ans, dp[(i, j)])
                
        return ans if ans >= 3 else 0


if __name__ == "__main__":

    sol = Solution()
    method = sol.lenLongestFibSubseq

    cases = [
        (method, ([1,2,3,4,5,6,7,8],), 5),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))