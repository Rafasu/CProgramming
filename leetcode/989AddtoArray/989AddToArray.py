# Schoolbook addition
# Solution: Add K to the last element and perform carry operations to the next number of the list.
# If list ended and still got carry, add the remainding digits to the list.
# Complexity: Time O(n) * (m) | Space O(m) where m is the carry.
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        carry = 0
        A[-1] += K
        for i in range(n - 1, -1, -1):
            A[i] += carry
            carry = A[i] // 10
            A[i] %= 10
    
        while(carry != 0):
            digit = carry % 10
            A.insert(0, digit)
            carry = carry // 10
            
        return A