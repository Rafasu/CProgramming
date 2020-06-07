# Excel Column Number
# Solution:  Used base conversion. 
# Assumptions: Will only receive capital letters and there will not be characters that aren't in the alphabet
# Complexity: Time O(n) | Space O(1)
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        size = len(A)
        number = 0
        power = size - 1
        for i in range(size):
            charNumber =  ord(A[i]) - 64
            number += (26 ** power) * charNumber
            power -= 1
        return number

