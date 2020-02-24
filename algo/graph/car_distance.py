"""

For each '0', find the distance to the closest 'C'. '#' means roadblock

Uber phone interview

"""

from collections import deque

input = [
    ['0', '0', '0', 'C', '#', '#'],
    ['C', '0', '0', '#', '0', '#'],
    ['#', '#', '#', '#', '0', '0'],
    ['C', '0', '0', '0', '0', '#'],
    ['0', '0', '0', '0', '#', '0']
]


def neighbors(x, y, grid):
    m, n = len(grid), len(grid[0])
    nei = []
    if x + 1 < m:
        nei.append((x + 1, y))
    if x - 1 >= 0:
        nei.append((x - 1, y))
    if y + 1 < n:
        nei.append((x, y + 1))
    if y - 1 >= 0:
        nei.append((x, y-1))
    return nei


def bfs(g):
    """
    
    BFS
    
    Unweighted graph. multi-source, multi-destination shortest path. 
    Because the graph is unweighted, a deque suffices. The element popped will always be the one
    with the shortest distance so far. For weighted graph, a heapq is needed to guarantee this

    """

    m, n = len(g), len(g[0])
    dist = [[float('inf')] * n for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    q = deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'C':
                q.append((i, j))
                dist[i][j] = 0
    
    # BFS
    while q:
        x, y = q.popleft()
        if not visited[x][y] and g[x][y] != '#':
            visited[x][y] = True
            for (nx, ny) in neighbors(x, y, g):
                if g[nx][ny] != '#' and not visited[nx][ny] and dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

print(bfs(input))