"""

639. 
Hard

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', 
which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        
        dp[i] is the number of ways to decode for substring s[:i]
        state transition: for substring s[:i], two cases. 
            1. the last element of the substring as a single string
            2. the last two elements of the substring as a single string.
        then the ways = ways_single_string * ways_of_shorter_substring_solved_prevsiouly 
        """
        MAX_NUM_CODING = 26
        MOD = 10**9+7
        
        def one_string_ways(c1, c2):
            
            if c1 == '0':
                return 0
            
            if '*' not in (c1, c2):
                if int(c1+c2) <= MAX_NUM_CODING:
                    return 1
                else:
                    return 0
        
            if not c2:
                return 9
            else:
                if c1+c2 == '**':
                    return 15
                elif c1 == '*':
                    if '0' <= c2 <= '6':
                        return 2
                    else:
                        return 1
                else:
                    if c1 == '1':
                        return 9
                    elif c1 == '2':
                        return 6
                    else:
                        return 0
        
        
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        elif s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            dp[i] = (one_string_ways(s[i-1], "")*dp[i-1] + one_string_ways(s[i-2], s[i-1])*dp[i-2]) % MOD
        
        return dp[-1]



# if __name__ == '__main__':

#     sol = Solution()
#     # method = sol.numDecodings
#     method = sol.dfs

#     cases = [
#         (method, ("ADOBECODEBANC", "ABC"), "BANC"),
#     ]

#     for i, (func, case, expected) in enumerate(cases):
#         ans = func(*case)
#         if ans == expected:
#             print("Case {:d} Passed".format(i + 1))
#         else:
#             print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))