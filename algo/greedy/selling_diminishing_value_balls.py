"""

1648.
Medium


"""

from typing import List
import math

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        inventory.sort(key = lambda x: -x)
        
        i = 0
        total = 0
        curr = inventory[0]
        c = 0
        n = len(inventory)

        while orders > 0:
            
            while c < n and inventory[c] == curr:
                c += 1
            
            if c == n:
                next_item = 0
            else:
                next_item = inventory[c]
            
            fulfilled = min(orders, c * (curr - next_item))

            # the number of rounds that a ball can be taken from all groups in the current batch `c`
            # after all these rounds complete, the lower bound is `curr - t + 1`
            # for example, 6 balls after 2 rounds, the lower bound is 6 - 2 + 1 = 5 balls
            t = curr - next_item

            # the number of groups from which an additional ball can be taken
            # the lower bound is t - 1
            r = 0

            if orders < c * (curr - next_item):
                t, r = divmod(orders, c)
            
            value = ((curr + curr - t + 1) * t // 2 * c + (curr - t) * r) % MOD
                
            total += value
            total = total % MOD
            orders -= fulfilled
            curr = next_item
        
        return total


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.maxProfit, ([2,5], 4), 14),
        (sol.maxProfit, ([3,5], 6), 19),
        (sol.maxProfit, ([497978859,167261111,483575207,591815159], 836556809), 373219333),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))