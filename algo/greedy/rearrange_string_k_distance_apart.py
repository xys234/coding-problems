"""

358.
Hard

Given a non-empty string str and an integer k, rearrange the string such that the same characters 
are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, 
return an empty string "".

Example 1:
str = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
str = "aaabc", k = 3 

Answer: ""

It is not possible to rearrange the string.
Example 3:
str = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.


"""
import heapq
from collections import Counter

class Solution:
    def rearrangeString(self, S: str, k: int):
        """
        
        Greedy. how to find the next element that has not appeared in the last (k-1) entries
        """
        n = len(S)
        count = Counter(S)
        max_count = 0
        pairs = []
        for s, c in count.items():
            pairs.append([-c, s])
            max_count = max(max_count, c)
        
        if max_count >= n // k + 1:
            return ""
        
        save = []
        ans = []
        heapq.heapify(pairs)
        
        while pairs:
            curr = heapq.heappop(pairs)
            save.clear()
            while len(ans) > 0 and curr[1] in ans[-k+1:]:
                save.append(curr)
                curr = heapq.heappop(pairs)

            ans.append(curr[1])
            curr[0] += 1
            for p in save:
                heapq.heappush(pairs, p)            
            if curr[0] < 0:
                heapq.heappush(pairs, curr)
        
        return "".join(ans)


if __name__ == '__main__':

    sol = Solution()
    method = sol.rearrangeString

    cases = [
        (method, ("aaadbbcc", 2), ("abacabcd", "abcabcad", "abcabcda")),
        (method, ("aabbcc", 3), "abcabc"),
        (method, ("aaabc", 3), ""),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans in expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))