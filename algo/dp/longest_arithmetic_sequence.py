"""

1027
Medium

Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] 
with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic 
if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].


"""

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        
        dp[i] is all the possible (step, length) pairs that use element A[i]
        state transition: append A[i] to all possible sequences ending at j for all j < i
        """

        dp = [{} for _ in range(len(A))]
        max_seq = 0
        
        i = 1
        while i < len(A):
            
            for j in range(i):
                diff = A[i] - A[j] 
                seq = dp[j].get(diff, 1) + 1
                dp[i][diff] = seq
                max_seq = max(max_seq, seq)
            
            i += 1

        return max_seq