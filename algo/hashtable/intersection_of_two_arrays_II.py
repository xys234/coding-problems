"""

350.
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

1. What if the given array is already sorted? How would you optimize your algorithm?
Ans: Use the binary search algorithm. 

2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
Ans: If arrays are not sorted, use the hash table solution. 

3. What if elements of nums2 are stored on disk, and the memory is limited 
such that you cannot load all elements into the memory at once?

Ans: 
If only nums2 is too big for the memory, the hash table solution still works. 
If both arrays are too big for the memory, use external sort to sort both arrays. 
Load the arrays by chunk and run the two-pointer algorithm. If one array is exhausted,
load the next chunk from that array. 

"""

import bisect
from collections import Counter


class Solution:
    def intersect_hashtable(self, nums1, nums2):
        """
        
        hash table solution.
        Put nums1 in a hash table and check if each element in nums2 is in the hash table.

        Time: O(m+n)
        Space: O(m)
        
        """

        m, n = len(nums1), len(nums2)
        # assume nums2 is the longer array
        if m > n:
            return self.intersect(nums2, nums1)

        c1 = Counter(nums1)
        
        res = []
        for num in nums2:
            if num in c1:
                
                # add to the result
                res.append(num)
                
                # update the count
                c1[num] -= 1
                if c1[num] == 0:
                    c1.pop(num)

        return res

    def intersect_two_pointer(self, nums1, nums2):
        """
        
        Assume both arrays are sorted

        Time: O(m+n)
        Space: O(1)

        """

        nums1.sort()
        nums2.sort()
        
        res = []
        p1, p2 = 0, 0
        m, n = len(nums1), len(nums2)
        while p1 < m and p2 < n:
            n1, n2 = nums1[p1], nums2[p2]
            if n1 == n2:
                res.append(n1)
                p1 += 1
                p2 += 1
            elif n1 < n2:
                p1 += 1
            else:
                p2 += 1
            
        return res

    def intersect_binary_search(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        
        binary search if both arrays are already sorted. 
        for each element in the shorter array, find the first appearance in the longer array. 
        then move the lower bound of the binary search to avoid duplicates
        
        Time: O(mlog(n))
        Space: O(1)
        """
        
        
        m, n = len(nums1), len(nums2)
        # assume nums2 is the longer array
        if m > n:
            return self.intersect(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        
        l2, h2 = 0, n
        
        res = []
        for n1 in nums1:
            ind = self.find_first_element(nums2, n1, l2, h2)
            if ind >= 0:
                res.append(n1)
                l2 = ind + 1
        
        return res
    
    def find_first_element(self, nums, target, lo, hi):
        """
        Find the size of the subarray with value target between lo and hi
        """
        
        l = bisect.bisect_left(nums, target, lo, hi)
        if l < len(nums) and nums[l] == target:
            return l
        return -1