# Using Array to compute
# Solution: Time O(n) | Space O(1) 
class Solution:
    def fib(self, N: int) -> int:
        lastTwo = [0, 1]
        count = 2
        while(count <= N):
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
            count += 1
            
        return lastTwo[1] if N >= 1 else lastTwo[0] 

# Runtime: 32 ms, faster than 37.75% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.

# Using Memoization 
# Solution: Time O(n) | Space O(n)
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]

# Runtime: 32 ms, faster than 37.75% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.
            