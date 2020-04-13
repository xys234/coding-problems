"""

1039. 
Medium

2020.03.28: Solved on hint 1

"""

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        
        # dp(i, j) is the best partition from node i to node j inclusive
        
        def dp(i, j, mem):
            if (i, j) in mem:
                return mem[(i, j)]
            
            if j - i == 1:
                s = 0
                mem[(i, j)] = s
                return s
            
            if j - i == 2:
                s = A[i]*A[i+1]*A[j]
                mem[(i, j)] = s
                return s
            
            min_score = float('inf')
            for k in range(i+1, j):
                s = A[i]*A[k]*A[j] + dp(i, k, mem) + dp(k, j, mem) 
                if s < min_score:
                    min_score = s
            mem[(i, j)] = min_score
            return min_score
        
        mem = {}
        return dp(0, n-1, mem)