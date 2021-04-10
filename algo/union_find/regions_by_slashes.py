"""

LC.959
Medium




"""

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        # total number of triangles in the square grid
        ufs = UnionFindSet(4 * n * n)

        for r in range(n):
            for c in range(n):
                
                # index of triangle 0 (top) in clockwise order
                index = 4 * (r * n + c)

                if grid[r][c] == '/':
                    ufs.union(index + 0, index + 3)
                    ufs.union(index + 1, index + 2)
                elif grid[r][c] == '\\':
                    ufs.union(index + 0, index + 1)
                    ufs.union(index + 2, index + 3)
                elif grid[r][c] == ' ':
                    ufs.union(index + 0, index + 1)
                    ufs.union(index + 1, index + 2)
                    ufs.union(index + 2, index + 3)
                
                # merge with the square in the neighboring row
                if r + 1 < n:
                    ufs.union(index + 2, index + 4 * n + 0)
                
                if c + 1 < n:
                    ufs.union(index + 1, index + 4 + 3)

        ans = 0
        for i in range(4 * n * n):
            if ufs.find(i) == i:
                ans += 1
        
        return ans


class UnionFindSet:
    """
    Union find set for n items
    
    """


    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0]*n
    
    def find(self, x):
        """
        Find the parent for item `x`
        """
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x, y) -> bool:
        """
        Union by rank. 

        rank is a descriptor for tree complexity. 
        returns False (union operation is not conducted) if the two items already in the same set 
        otherwise union and return True
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True
        

if __name__ == "__main__":

    sol = Solution()
    method = sol.regionsBySlashes

    cases = [
        # (method, ([" /", "/ "],), 2),
        # (method, (["\\/", "/\\"],), 4),
        (method, (["\\/\\ "," /\\/"," \\/ ","/ / "],), 3),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))