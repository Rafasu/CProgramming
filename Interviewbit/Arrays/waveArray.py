# Solution: Sort the array and shift pairs (i, i+1)
# Complexity: O(nlogn) | Space O(1)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        for i in range(0, n, 2):
            if i + 1 < n:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
        return A