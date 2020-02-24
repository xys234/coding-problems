"""

767.
Medium

"""


import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        
        Greedy. Always process the most frequent character. if the current most frequent
        is the same as previous one. Pick the next one. 
        """
        n = len(S)
        count = Counter(S)
        max_count = 0
        pairs = []
        for s, c in count.items():
            pairs.append([-c, s])
            max_count = max(max_count, c)
        
        if n % 2 == 0 and max_count >= n // 2 + 1:
            return ""
        
        if n % 2 == 1 and max_count > n // 2 + 1:
            return ""
        
        prev = None
        ans = []
        heapq.heapify(pairs)
        
        while pairs:
            curr = heapq.heappop(pairs)
            if prev and curr[1] == prev:
                save = curr
                curr = heapq.heappop(pairs)
                heapq.heappush(pairs, save)
            
            ans.append(curr[1])
            prev = curr[1]
            curr[0] += 1
            if curr[0] < 0:
                heapq.heappush(pairs, curr)
        
        return "".join(ans)
    

if __name__ == '__main__':

    sol = Solution()
    method = sol.reorganizeString

    cases = [

        (method, ("aab",), "aba"),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
        
        
        