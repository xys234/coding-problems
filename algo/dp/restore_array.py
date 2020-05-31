"""

1416.
Hard


A program was supposed to print an array of integers. 
The program forgot to print whitespaces and the array is printed as a string of digits 
and all we know is that all integers in the array were in the range [1, k] 
and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]


"""


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        
        
        """
        n = len(s)
        MOD = 10**9+7
        
        dp = [0 for _ in range(n+1)]
        dp[-1] = 1
        
        nums = [int(c) for c in s] + [float('inf')]
        
        for i in range(n-1, -1, -1):
            j = i + 1
            curr = nums[i]
            while j <= n and 1 <= curr <= k:
                dp[i] = (dp[i] + dp[j]) % MOD
                curr = curr * 10 + nums[j]
                j += 1
        
        return dp[0]
            
                
                