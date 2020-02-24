"""


"""

from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        positions = {}
        for i, ch in enumerate(S):
            if ch in positions:
                if i > positions[ch]:
                    positions[ch] = i
            else:
                positions[ch] = i

        partitions = []
        i = 0
        while i < len(S):
            pos = positions[S[i]]
            j = i + 1
            while j < pos:
                if positions[S[j]] > pos:
                    pos = positions[S[j]]
                j += 1
            partitions.append(pos)
            i = pos + 1

        partitions = [0] + [p + 1 for p in partitions]
        partitions = [p2 - p1 for p2, p1 in zip(partitions[1:], partitions[:-1])]
        return partitions
    
    def partitionLabels2(self, S: str) -> List[int]:
        """
        
        Greedy algorithm. Find the longest partition possible each i
        """
        d = {}
        start, end = 0, 0
        for i, s in enumerate(S):
            if s not in d:
                start = end = i
                d[s] = [start, end]
            else:
                d[s][1] = i
        
        ans = []
        i = 0
        while i < len(S):
            s = S[i]
            start, end = d[s]
            j = start + 1
            while j <= end:
                end = max(end, d[S[j]][1])
                j += 1
            # print(start, end)
            ans.append(end-start+1)
            # print(ans)
            i = end+1
        return ans
                        
if __name__ == '__main__':

    sol = Solution()
    method = sol.partitionLabels2

    cases = [

        (method, ("qiejxqfnqceocmy",), [13, 1, 1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))