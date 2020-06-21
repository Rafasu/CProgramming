# Solution: Return the start/low of the binary search because it will be pointing always to the place where
# The element should be.
# Complexity: Time O(log n) | Space O(1)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start = 0 
        end =  len(A) -  1
        while(start <=  end):
            mid = start + ( end - start) //2
            if(A[mid] ==  B):
                return mid
            elif(A[mid] < B):
                start = mid + 1
            else:
                end = mid - 1
        return start
                