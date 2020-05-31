"""

1234.
Medium

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times 
where n is the length of the string.

Return the minimum length of the substring 
that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".



"""

from collections import Counter

class Window:
    def __init__(self):
        self.counter = [Counter()]
    
    def add(self, x):
        self.counter[x] += 1
    
    def remove(self, x):
        self.counter[x] -= 1
    
    def cover(self, target):
        for k in target:
            if self.counter[k] < target[k]:
                return False
        return True

class Solution:
    def balancedString(self, s: str) -> int:
        c = Counter(s)
        n = len(s)
        balanced = Counter({ch:n//4 for ch in ('Q','R','W','E')})
        target = Counter({ch:c[ch]-balanced[ch] for ch in ('Q','R','W','E') if c[ch]-balanced[ch] > 0})
        
        if not target:
            return 0
        
        # print(target)
        
        l = r = 0
        w = Window()
        minlen = n + 1

        while r < n:
            w.add(s[r])

            while l < r and w.cover(target):
                minlen = min(minlen, r-l+1)
                w.remove(s[l])
                l += 1
            
            if w.cover(target):
                minlen = min(minlen, r-l+1)
            
            r += 1
        return minlen



if __name__ == '__main__':

    sol = Solution()
    method = sol.balancedString

    cases = [
        (method, ("eceba", 3), 4),
        (method, ("bcaaaaa", 2), 6),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

