


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        n = len(tiles)
        total = [0]
        
        def dfs(curr, l, total):
            
            if len(curr) == l:
                print(curr)
                total[0] += 1
                return
            
            prev = -1
            for i in range(len(tiles)):
                if not used[i] and (prev < 0 or tiles[i] != tiles[prev]):
                    used[i] = True
                    dfs(curr + [tiles[i]], l, total)
                    used[i] = False
                    prev = i
        
        for l in range(1, n + 1):
            used = [False] * n
            dfs([], l, total)
        
        return total[0]


if __name__ == '__main__':

    sol = Solution()
    method = sol.numTilePossibilities


    cases = [

        (method, ("AAB", ), 8),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))