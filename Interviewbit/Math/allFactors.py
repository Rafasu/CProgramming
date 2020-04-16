# Solution: So the solution is based on this video: https://www.youtube.com/watch?v=dolcMgiJ7I0&feature=emb_err_watch_on_yt
# Complexity: Time O(nlogn) | Space O(squareroot(n) * 2)
import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        n = int(math.sqrt(A))
        factors = []
        for i in range(1, n+1):
            if(A % i == 0):
                factors.append(i)
                if(A / i != n):
                    factors.append(A/i)
        factors.sort()
        return factors

# Optimized time complexity
# Time O(squareroot(n))
import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        n = int(math.sqrt(A))
        factors = []
        lastFactors = []
        for i in range(1, n+1):
            if(A % i == 0):
                factors.append(i)
                if(A / i != n):
                    lastFactors.append(A/i)
                    #factors.append(A/i)
        k = len(lastFactors)
        for i in range(k-1, -1, -1):
            factors.append(lastFactors[i])   
        # factors.sort()
        return factors
