# Solution: Dicionary O(n) time | O(n) space
#

def getNthFibonacci(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibonacci(n - 1, memoize) + getNthFibonacci(n - 2, memoize)
        return memoize[n]

# Solution: Using array
def nthFibonacci(n):
    lastTwo = [0, 1]
    counter = 2
    while(counter <= n):
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
