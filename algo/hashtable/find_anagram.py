"""

438. Find all anagrams in a string
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and 
p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        cp, np, ns, cs = Counter(p), len(p), len(s), Counter()
        if ns < np:
            return []

        ans = []
        for i, c in enumerate(s):
            if i < np:
                cs[c] += 1
            else:
                if cs == cp:
                    ans.append(i - np)
                if cs[s[i-np]] == 1:
                    cs.pop(s[i - np])
                else:
                    cs[s[i - np]] -= 1
                cs[c] += 1

        if cp == cs:
            ans.append(ns-np)
        return ans
    
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        """
        
        Sliding window.
        2020.02.23: Fixed window length. Window state maintained by a hashtable
        """
        cp = Counter(p)
        k, n = len(p), len(s)
        
        
        if k > len(s):
            return []
        
        ans = []
        curr = Counter(s[:k])
        pos = k
        
        # a window of length k
        while pos < n:
            # print(pos, curr)
            if curr == cp:
                ans.append(pos-k)
                
            # element leaving the window
            if curr[s[pos-k]] == 1:
                curr.pop(s[pos-k])
            else:
                curr[s[pos-k]] -= 1

            # element entering the window
            if s[pos] in curr:
                curr[s[pos]] += 1
            else:
                curr[s[pos]] = 1
            pos += 1

        # check the last window
        if curr == cp:
            ans.append(pos-k)
        return ans



if __name__=='__main__':

    sol = Solution()
    method = sol.findAnagrams

    cases = [
        (method, ("cbaebabacd", "abc"), [0,6]),
        (method, ("baa", "aa"), [1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))