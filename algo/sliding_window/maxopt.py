from collections import Counter

class Window:
    def __init__(self, ch):

        self.min_ch = ch
        self.max_ch = ch
        self.min_count = 1
        self.max_count = 1
        self.size = 1

        self.d = Counter(ch)

    def update_count(self, total_count):

        min_count, max_count = float('inf'), -float('inf')
        min_ch, max_ch = None, None

        for k, c in self.d.items():
            if c < min_count:
                min_ch = k
                min_count = c

            elif c > max_count:
                max_ch = k
                max_count = c

            elif total_count[k] > total_count[max_ch]:
                max_ch = k
                max_count = c
            
            self.min_ch, self.min_count = min_ch, min_count
            self.max_ch, self.max_count = max_ch, max_count

    def is_valid(self, total_count):

        return len(self.d) == 1 or len(self.d) <= 2 and self.min_count <= 1 and self.max_count < total_count[self.max_ch]

    def add(self, ch, total_count):
        self.d[ch] += 1
        self.size += 1
        self.update_count(total_count)

    def pop(self, ch, total_count):
        self.size -= 1
        if self.d[ch] == 1:
            self.d.pop(ch)
        else:
            self.d[ch] -= 1
        self.update_count(total_count)

class Solution: 
    
    def maxRepOpt1(self, text: str) -> int:
        
        count = Counter(text)
        
        n = len(text)
        i = 0
        j = 1
        w = Window(text[i:j])
        max_len = 1
        max_w = None
        while j < n:
            
            w.add(text[j], count)
            if w.is_valid(count):
                max_len = max(max_len, w.size)
                max_w = len(w.d)
            else:
                while j < n and i < j and not w.is_valid(count):
                    w.pop(text[i], count)
                    i += 1
            j += 1
        
        if max_len == n and max_w == 2:
            return max_len - 1
        else:
            return max_len
            
            
if __name__ == "__main__":
    sol = Solution()
    method = sol.maxRepOpt1

    cases = [
        (method, ('ababa',), 3),
        (method, ('aaabaaa',), 6),
        (method, ('aaaaaa',), 6),
        (method, ('abcdef',), 1),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))