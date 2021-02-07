# Solution: Sort array and check the number of rigth elements are the same as the element
# Complexity: Time O(n log n) | Space O(1)
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n-1):
            # Duplicate elements are equal so they don't count
            if(A[i] == A[i + 1]):
                continue
            # Last ocurrence
            if(A[i] == (n - i - 1) ):
                return 1
        # Edge case: Last element is zero
        if(A[-1] == 0):
            return 1
        return -1
