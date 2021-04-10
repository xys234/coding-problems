"""

1025. Divisor Game
Easy


"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        mem = {1:False, 2:True}
        outcome = self.helper(N, mem, 'A')
        print(mem)
        return outcome
        
    def helper(self, N, mem, player):
        
        if N in mem:
            return mem[N]
        
        next_player = 'B' if player == 'A' else 'A'
        for fac in range(1, N):
            if N % fac == 0:
                print(N, fac, next_player)
                outcome = self.helper(N - fac, mem, next_player)
                if next_player == 'A':
                    if outcome:
                        mem[N] = outcome
                        return mem[N]
        mem[N] = False
        return mem[N]


sol = Solution()
print(sol.divisorGame(4))