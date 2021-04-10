"""

Lintcode

Amazon

"""


from collections import deque

class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def searchSubarray(self, arr, k):
        # Write your code here
        
        window = deque()
        curr = 0
        for num in arr:
            if not window or curr < k:
                window.append(num)
                curr += num
            elif curr > k:
                while curr > k:
                    p = window.popleft()
                    curr -= p
            else:
                return len(window)
        return len(window) if curr == k else -1
    


if __name__ == "__main__":

    sol = Solution()
    method = sol.searchSubarray

    cases = [
        # (method, ([1,2,3,4,5],9), 3),
        (method, ([1,-1,0],0), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))