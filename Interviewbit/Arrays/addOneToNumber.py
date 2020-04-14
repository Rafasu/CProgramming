# Add One to Array
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        carry = (A[n-1] + 1)// 10
        A[n-1] += 1
        A[n-1] %= 10
        for i in range(n-2, -1, -1):
            if(carry > 0):
                A[i] += carry
                carry = A[i] // 10
                A[i] %= 10
        if(carry > 0):
            A.insert(0, carry)
        # Delete zero's at the beginning of the list
        j = 0
        while(A[j] == 0):
            j += 1
        return A[j:]