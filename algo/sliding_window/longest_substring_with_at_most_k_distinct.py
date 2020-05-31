"""

LC.340. (LT 386)
Hard

Description

Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"

Challenge
O(n) time


2020.05.08: LT accepted. 

"""

from collections import Counter


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        class Window:
            def __init__(self):
                self.counter = Counter()
            
            def add(self, s):
                self.counter[s] += 1
            
            def remove(self, s):
                self.counter[s] -= 1
                if self.counter[s] == 0:
                    self.counter.pop(s)
            
            @property
            def nunique(self):
                return len(self.counter)

        if k == 0 or not s:
            return 0

        n = len(s)
        l = r = 0
        w = Window()
        maxlen = 0
        while r < n:
            w.add(s[r])
            
            while l < r and w.nunique > k:
                w.remove(s[l])
                l += 1

            currlen = r - l + 1
            maxlen = max(maxlen, currlen)
            r += 1

        return maxlen


if __name__ == '__main__':

    sol = Solution()
    method = sol.lengthOfLongestSubstringKDistinct

    cases = [
        (method, ("eceba", 3), 4),
        (method, ("bcaaaaa", 2), 6),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
            
