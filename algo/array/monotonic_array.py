"""

896.
Easy

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.


"""



class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool

        Pure iteration.

        """
        i = 0
        decreasing, increasing = False, False
        while i <= len(A)-2:
            if A[i] < A[i+1]:
                increasing = True
            elif A[i] > A[i+1]:
                decreasing = True
            if increasing and decreasing:
                return False
            i += 1
        return True


if __name__ == '__main__':
    # case = [1,2,3,3]
    # case = [6,5,4,4]
    case = [11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
    sol = Solution()
    print(sol.isMonotonic(case))
