"""

76.
Hard


Given a string S and a string T, find the minimum window in S 
which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern = Counter(t)
        
        i, j = 0, 0
        curr = Counter()
        minlen = len(s) + 1
        minstr = ""
        required = len(pattern)
        formed = 0
        
        while j < len(s):
            
            curr[s[j]] += 1
            if s[j] in pattern and curr[s[j]] == pattern[s[j]]:
                formed += 1

            while i <= j and formed == required:
                if j-i+1 < minlen:
                    minstr = s[i:j+1]
                    minlen = j - i + 1
                
                # removed the leftmost character
                curr[s[i]] -= 1
                if s[i] in pattern and curr[s[i]] < pattern[s[i]]:
                    formed -= 1
                
                i += 1
            
            j += 1
            
        return minstr


if __name__ == '__main__':

    sol = Solution()
    method = sol.minWindow

    cases = [
        (method, ("ADOBECODEBANC", "ABC"), "BANC"),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))