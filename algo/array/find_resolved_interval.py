"""
Find "resolved" interval, resolved marked as 1. input [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]    output [(2,4), (7,7), (9,10)] 
Find the start and ending indices of consecutive resolved interval

Facebook Infra DS phone interview

"""

class Solution:
    def find_resolved_interval(self, intervals):
        i = 0
        ans = []
        while i < len(intervals):
            if intervals[i] == 0:
                i += 1
            else:
                j = i
                while j < len(intervals):
                    if intervals[j] == 1:
                        j += 1
                    else:
                        break
                ans.append((i, j-1))
                i = j
        return ans


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.find_resolved_interval, ([0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],), [(2,4), (7,7), (9,10)]),
        (sol.find_resolved_interval, ([0, 0],), []),
        (sol.find_resolved_interval, ([1],), [(0, 0)]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
