"""
32.
Hard

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


2018.
2020.05.31

"""



class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0]*len(s)     # dp[i] ~ the length of the valid parentheses at index i
        max_dp = 0
        for i in range(1, len(s)):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            elif s[i] == ")" and s[i-1] == ")" and i-dp[i-1]-1>=0:
                if s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
            max_dp = max(max_dp, dp[i])
        return max_dp

    def longestValidParentheses2(self, s):
        """
        
        dp[i] is the length of the longest of the substring ending at i including s[i]
        state transition: 
          1. if s[i] == '(', dp[i] = 0
          2. if s[i] == ')', 
            2.1 if s[i-1] == '('
            2.2 if s[i-1] == ')'
        
        Time: O(n); Space O(n)

        """

        n = len(s)
        dp = [0 for _ in range(n)]
        maxlen = 0
        
        for i, c in enumerate(s):
            if i > 0 and c == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + dp[i-1-dp[i-1]-1] + 2
                maxlen = max(maxlen, dp[i])    
                
        return maxlen

if __name__=="__main__":
    sol = Solution()
    method = sol.longestValidParentheses2

    cases = [
        (method, ("(()",), 2),
        (method, ("(()())",), 6),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

