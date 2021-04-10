"""

388.
Medium

2020-01-13: 92.8%

"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        prev = 0
        files = []
        n = len(input)
        
        for i in range(n):
            if input[i] == '\n' or i == n - 1:
                if i == n - 1:
                    curr = input[prev:i+1]
                else:
                    curr = input[prev:i]
                level = self.get_level(curr)
                if curr.startswith('\n'):
                    curr = curr[level+1:]
                
                while stack and stack[-1][0] >= level:
                    stack.pop()
                
                if curr.find('.') > 0:   
                    files.append('/'.join([p[1] for p in stack] + [curr]))
                    
                stack.append((level, curr))
                
                print(stack)
                prev = i
            
        print(files)
        return max([len(f) for f in files]) if files else 0 
    
    def get_level(self, s):
        right = s.rfind('\t')
        left = s.find('\t')
        if left == -1:
            return 0
        return right - left + 1


if __name__ == "__main__":

    sol = Solution()
    method = sol.lengthLongestPath

    cases = [
        (method, ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",), 32),
        (method, ("file1.txt\nfile2.txt\nlongfile.txt",), 12),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))