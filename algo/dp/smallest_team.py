"""

1125.
Hard

"""

from typing import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        # build skill bitmask for each person
        skill_map = {s:i for i, s in enumerate(req_skills)}
        skills = []
        
        for person in people:
            bm = 0
            for skill in person:
                ind = skill_map[skill]
                bm = bm | (1 << ind)
            skills.append(bm)
            
        # print([bin(s) for s in skills])
        
        # 0-1 knapsack
        # dp[j] use first i people to make skill set j
        n, p = len(req_skills), len(people)
        target = (1 << n) - 1

        # padded dp array
        dp = [float('inf') for _ in range(1 << n)]
        parents = [None for _ in range(1 << n)]
        dp[0] = 0
        
        for i in range(p):
            skill = skills[i]
            if skill == 0:
                continue
            
            for j in range(target, -1, -1):
                if dp[j] + 1 < dp[j | skill]:
                    dp[j | skill] = dp[j] + 1
                    parents[j | skill] = (j, i)
        
        # print(dp)
        # print(parents)
        ans = []
        curr = target
        while curr > 0:
            ans.append(parents[curr][1])
            curr = parents[curr][0]
        return list(reversed(ans))


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.smallestSufficientTeam, (
            ["algorithms","math","java","reactjs","csharp","aws"], 
            [
                ["algorithms","math","java"],
                ["algorithms","math","reactjs"],
                ["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]
            ]
        ), [1,2]),
        (sol.smallestSufficientTeam, (
                ["java","nodejs","reactjs"], 
                [["java"],["nodejs"],["nodejs","reactjs"]]
            ), [0,2]),

        ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))