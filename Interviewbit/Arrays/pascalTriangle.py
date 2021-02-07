# Solution: Make a Pascal Triangle.
# First iterator goes from 2 row that is where the pascal starts to change from 1s
# And second iterator omits the first and the last number of each row of the pascal triangle, which are 1s
# The construction for the other numbers is given in the problem.

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        pascal_triangle = []

        for i in range(A):
            pascal_triangle.append([1]*(i+1))
      
        for i in range(2,A):
            for j in range(1,i):
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
    
        return pascal_triangle
