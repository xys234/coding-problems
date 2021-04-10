"""

722. Remove Comments
Medium

Note that C++ does not allow nested block comments

"""


from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        i = j = 0
        n = len(source)
        
        res = []
        while i < n:
            stmt = source[i]
            line_comment_ind = stmt.find("//")
            block_comment_ind = stmt.find("/*")
            
            
            if line_comment_ind < 0 and block_comment_ind < 0:
                res.append(stmt)
                i += 1
            elif line_comment_ind >= 0 and (block_comment_ind < 0 or block_comment_ind > line_comment_ind):
                res.append(stmt[:line_comment_ind])
                i += 1
            elif block_comment_ind >= 0 and block_comment_ind > line_comment_ind:
                j = i
                close_block_comment_ind = -1
                while j < n and close_block_comment_ind < 0:
                    if j != i:
                        close_block_comment_ind = source[j].find("*/")
                    else:
                        close_block_comment_ind = source[j].find("*/", block_comment_ind + 2)
                    if close_block_comment_ind >= 0:
                        break
                    j += 1
                
                # print(j, n)
                
                if j == i:
                    stmt = stmt[:block_comment_ind] + stmt[close_block_comment_ind+2:]
                    if stmt:
                        res.append(stmt)
                    i += 1
                elif j < n:
                    temp = ""
                    if block_comment_ind > 0:
                        temp += stmt[:block_comment_ind]
                    if close_block_comment_ind+2 < len(source[j]):
                        temp += source[j][close_block_comment_ind+2:]
                    
                    if temp:
                        res.append("".join(temp))
                    i = j + 1
                else:
                    i += 1
        
        return res



if __name__ == "__main__":

    sol = Solution()
    method = sol.removeComments

    cases = [
        (method, (["main() { ", "  int a = 1; /* Its comments here ", "", "  ", "  */ return 0;", "} "],), ["main() { ","  int a = 1;  return 0;","} "]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))