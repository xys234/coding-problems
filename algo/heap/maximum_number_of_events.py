"""

1353.
Medium


"""

from typing import List

import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse = 1)
        
        # print(events)
        
        minHeap = []
        ans = 0

        while events or minHeap:
            if not minHeap: 
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(minHeap, events.pop()[1])
            
            # attend the event with earliest end time. greedy
            heapq.heappop(minHeap)
            ans += 1
            
            # remaining events with end time earlier than d, we cannot attend
            while minHeap and minHeap[0] <= d:
                heapq.heappop(minHeap)
            d += 1
        return ans


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.maxEvents, ([[1,5],[1,5],[1,5],[2,3],[2,3]], ), 5),
        (sol.maxEvents, ([[1,1],[1,1],[2,5],[2,2],[3,8]], ), 5),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))