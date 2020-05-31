"""

1402
Hard

2020.05.28: Suffix DP. Running suffix sum.

"""

from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        
        
        """
        n = len(satisfaction)
        satisfaction.sort()
        
        suffix = curr = ans = 0
        for j in reversed(range(n)):
            suffix += satisfaction[j]
            curr += suffix
            ans = max(ans, curr)

        return ans
                    

if __name__ == '__main__':

    sol = Solution()
    method = sol.maxSatisfaction

    cases = [
        (method, ([-1,-8,0,5,-9], ), 14),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))