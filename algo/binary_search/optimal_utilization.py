"""

optimal utilization

Amazon OA 2019 
https://leetcode.com/discuss/interview-question/373202

Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
Example 3:

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]
Example 4:

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]

"""

import bisect
from typing import List

class Solution:
    def closest_pairs(self, a: List[int], b: List[int], target: int) -> List[List[int]]:
        """
        
        Binary search. 
        For each element in a, find the largest element in b closest to target using binary search
        """

        a = [list(reversed(e)) for e in a]
        b = [list(reversed(e)) for e in b]

        na, nb = len(a), len(b)

        closest = float('inf')
        ans = []

        for v, i in a:
            t = target - v
            ind = bisect.bisect_right(b, [t, -1])
            ind = min(ind, nb-1)
            bv, bi = b[ind]
            if bv > t: 
                if ind >= 1:
                    bv, bi = b[ind-1]
                else:
                    continue
            diff = target - (v + bv) 
            if diff >= 0:
                if diff < closest:
                    closest = diff
                    ans.clear()
                ans.append([i, bi])
        return ans
                        
if __name__ == '__main__':

    sol = Solution()
    method = sol.closest_pairs

    cases = [

        (method, ([[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20), [[3, 1]]),
        (method, ([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7), [[2, 1]]),
        (method, ([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10), [[2, 4], [3, 2]]),
        (method, ([[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20), [[1, 3], [3, 2]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))

