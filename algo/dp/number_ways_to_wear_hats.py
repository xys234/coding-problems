"""

1434
Hard


2020.05.12: Study solution. Bitmask + DP

"""

from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        preferences = [[] for _ in range(40)]
        for i, hat in enumerate(hats):
            for h in hat:
                preferences[h-1].append(i)
        
        MOD = 10**9+7

        # i-th digit represents whether i-th person has already had a hat
        # dp[j] is the number of ways to assign hats for pattern j
        dp = [0]*(1<<n)
        dp[0] = 1

        # starting from pattern 11...1 is because dp[111] += dp[110] 
        # if person 0 prefers the hat that is being assigned and the number of ways is equal to dp[110]
        # and the state becomes "111"
        # the intuition is that assign all possible hats to only one person and no need to consider how we arrive
        # at this pattern. So even if the iteration starts with pattern with more 1's, 
        # the solution for these patterns relies on those with fewer 1's. 
        for h in range(40):
            for j in range((1<<n)-1, -1, -1):
                for p in preferences[h]:
                    if (j & (1 << p)) == 0:
                        dp[j | (1 << p)] += dp[j]
                        dp[j | (1 << p)] %= MOD
                    
        return dp[(1<<n)-1]

if __name__ == '__main__':

    sol = Solution()
    method = sol.numberWays

    cases = [
        (method, ([[3,5,1],[3,5]],), 4),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
