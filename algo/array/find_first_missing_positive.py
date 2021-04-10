"""

41.
Hard

"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # expected: 1 to n
        count_in_range = 0
        min_elem, max_elem = n, 1
        
        for num in nums:
            if 1 <= num <= n:
                min_elem = min(min_elem, num)
                max_elem = max(max_elem, num)
                count_in_range += 1
            
        if count_in_range == 0:
            return 1
        
        # if count_in_range == n and min_elem == 1 and max_elem == n:
        #     return n + 1
        
        for i in range(n):
            if nums[i] == i + 1:
                nums[i] = 'v'
            
            
            elif nums[i] != 'v' and 1 <= nums[i] <= n:
                next_pos = nums[i] - 1
                
                while nums[next_pos] != 'v' and 1 <= nums[next_pos] <= n:
                    temp = nums[next_pos]
                    nums[next_pos] = 'v'
                    next_pos = temp - 1
                
                # previous position is a valid number. therefore the current position needs to be marked
                if nums[next_pos] != 'v':
                    nums[next_pos] = 'v'
                if nums[i] != 'v':
                    nums[nums[i] - 1] = 'v'
                
        # print(nums)
        
        for i in range(n):
            if nums[i] != 'v':
                return i + 1
        
        return n + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:

        n = len(nums)
        if 1 not in nums:
            return 1
        
        # replace <= 0
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 1
        
        # mark the elements that are present
        for i in range(n):
            index = abs(nums[i]) - 1
            if index < n:
                nums[index] = - abs(nums[index])
            
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
                

if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.firstMissingPositive, ([2,1], ), 3),
        (sol.firstMissingPositive, ([-1,4,2,1,9,10], ), 3),
        (sol.firstMissingPositive, ([0,1,2], ), 3),
        (sol.firstMissingPositive, ([1,1], ), 2),
        (sol.firstMissingPositive, ([3,1], ), 2),
        (sol.firstMissingPositive, ([1,1,1], ), 2),
        (sol.firstMissingPositive, ([1], ), 2),
      
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))