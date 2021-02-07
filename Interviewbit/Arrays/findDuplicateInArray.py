# Solution: Use a hashtable to see if the number is already in.
# Complexity: Time O(n) | Space O(n)
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        repeated = -1
        freq = {}
        for i in A:
            if(i in freq):
                repeated = i
            else:
                freq[i] = i
        return repeated
            
