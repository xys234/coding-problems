"""

130.
Medium

DFS

"""


from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return
        
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        status = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == 'O' and not visited[i][j]:
                    self.dfs(board, visited, status, i, j)
        
        print(status)
        
        for i in range(m):
            for j in range(n):
                if status[i][j] == 0:
                    board[i][j] = 'X'
    
    def neighbors(self, board, x, y):
        m, n = len(board), len(board[0])
        if x + 1 < m:
            yield x + 1, y
        if x - 1 >= 0:
            yield x - 1, y
        if y + 1 < n:
            yield x, y + 1
        if y - 1 >= 0:
            yield x, y - 1
    
    def dfs(self, board, visited, status, x, y):
        
        m, n = len(board), len(board[0])
        
        visited[x][y] = True
        status[x][y] = 1
        for nx, ny in self.neighbors(board, x, y):
            if board[nx][ny] == 'O' and not visited[x][y]:
                self.dfs(board, visited, status, nx, ny)


if __name__ == '__main__':

    sol = Solution()
    # sol.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
    sol.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])