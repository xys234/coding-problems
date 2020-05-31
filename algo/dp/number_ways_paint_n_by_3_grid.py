"""

1411.
Hard


2020.05.25: Own method after reading hints


"""


class Solution:
    def numOfWays(self, n: int) -> int:
        """
        
        How many 3-color combinations can one 3-color/2-color combination generates. 
        How many 2-color combinations can one 3-color/2-color combination generates
        
        """
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [6, 6]
        MOD = 10**9 + 7
        for i in range(1, n):
            dp[i][0] = (dp[i-1][0]*2 + dp[i-1][1]* 2) % MOD
            dp[i][1] = (dp[i-1][0]*2 + dp[i-1][1]* 3) % MOD
        return sum(dp[n-1]) % MOD
    