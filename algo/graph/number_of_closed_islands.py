"""

1254.
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  
An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        num_islands = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def land_neighbors(x, y):
            for nx, ny in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]:
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    yield nx, ny
        
        def dfs(x, y):
            visited[x][y] = True
            flag = True
            for nx, ny in land_neighbors(x, y):
                if nx in (0, m - 1) or ny in (0, n - 1):
                    flag = False
                else:
                    if not dfs(nx, ny):
                        flag = False
            return flag

        
        for x in range(1, m - 1):
            for y in range(1, n - 1):
                if grid[x][y] == 0 and not visited[x][y]:
                    
                    if dfs(x, y):
                        num_islands += 1
        
        return num_islands


if __name__ == "__main__":

    sol = Solution()
    method = sol.closedIsland

    cases = [

        (method, (
            [
                [0,0,1,1,0,1,0,0,1,0],
                [1,1,0,1,1,0,1,1,1,0],
                [1,0,1,1,1,0,0,1,1,0],
                [0,1,1,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,1,1,1,0],
                [0,1,0,1,0,1,0,1,1,1],
                [1,0,1,0,1,1,0,0,0,1],
                [1,1,1,1,1,1,0,0,0,0],
                [1,1,1,0,0,1,0,1,0,1],
                [1,1,1,0,1,1,0,1,1,0]
            ],), 5),

    ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))