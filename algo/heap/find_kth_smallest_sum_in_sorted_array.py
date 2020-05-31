"""

1439.
Hard


You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. 
Return the Kth smallest array sum among all possible arrays.

 

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12

2020.05.11: 78% after hint. 

"""

import heapq
from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        smallest = sum([row[0] for row in mat])
        q = [(smallest, [0 for _ in range(m)])]
        visited = set()
        ans = smallest
        

        while k > 0:
            smallest, indices = heapq.heappop(q)
            visited.add(tuple(indices))
            k -= 1
            ans = smallest
            next_smallest = smallest
            for r, ind in enumerate(indices):
                if ind < n - 1:
                    indices[r] += 1
                    if tuple(indices) not in visited:
                        next_smallest = smallest-mat[r][ind]+mat[r][ind+1]
                        print(next_smallest, indices)
                        heapq.heappush(q, (next_smallest, indices[:]))
                        visited.add(tuple(indices))
                    indices[r] -= 1
                    
        return ans


if __name__ == '__main__':

    sol = Solution()
    method = sol.kthSmallest

    cases = [
        (method, ([[1,3,11],[2,4,6]], 9), 17),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))