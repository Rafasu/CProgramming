# Solution: Check resulting shift(Left or right) and perform the shift.
# Complexity: Time O(n)| Space O(m) // Couldn't determine it really.
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = 0
        right_shift = 0
        n = len(s)
        newString = ''
        
        for elem in shift:
            if(elem[0] == 0):
                left_shift += elem[1]
            else:
                right_shift += elem[1]
                
        if(left_shift == right_shift):
            return s
        elif(left_shift - right_shift > 0):
            # Perform left shift
            k = left_shift - right_shift
            for j in range(n):
                newString += s[(j+k)%(n)]
        else:
            # Perform right shift
            k = right_shift - left_shift
            for j in range(n):
                newString += s[(n-k+j)%(n)]
                
        return newString