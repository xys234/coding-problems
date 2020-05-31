"""

343. Integer Break
Medium

Given a positive integer n, break it into the sum of at least two positive integers and
maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

2018.: 1st
2020.05.31: 

"""

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n-1)
        dp[0] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                if i-j < 2:
                    if j*(i-j) > dp[i-2]:
                        dp[i - 2] = j * (i-j)
                elif j*dp[i-j-2] > dp[i-2] or j*(i-j) > dp[i-2]:
                    dp[i-2] = j*max(dp[i-j-2], i-j)

        return dp[-1]

    def integerBreak2(self, n: int) -> int:
        """
        

        dp[i] is the maximum product for number i
        """
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1
        
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, j*(i-j))
        
        print(dp)
        return dp[-1]

if __name__ == "__main__":

    sol = Solution()

    