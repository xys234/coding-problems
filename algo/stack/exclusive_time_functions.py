"""
636.
Medium

"""

from typing import List


from collections import defaultdict

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def parse(l:str):
            data = l.split(":")
            ind, event, t = int(data[0]), data[1], int(data[2])
            return ind, event, t
        
        i0, e0, t0 = parse(logs[0])
        stack = [i0]
        latest = t0
        exclusive_times = defaultdict(int)
        
        for log in logs[1:]:
            ind, event, t = parse(log)
            
            if event == 'start':
                if stack:
                    exclusive_times[stack[-1]] += t - latest
                stack.append(ind)
                latest = t
            else:
                exclusive_times[stack[-1]] += t - latest + 1
                latest = t + 1   # translate the end time to the start of the next second
                stack.pop(-1)
        return list(exclusive_times.values())