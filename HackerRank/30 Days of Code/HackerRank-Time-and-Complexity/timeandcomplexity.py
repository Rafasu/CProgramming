# Simple Solution
import math
tests = int(input())

def isPrime(number):
    if number == 1:
        return False
    else:
        sqr =  math.floor(math.sqrt(number))
        for i in range(2, sqr+1):
            if number % i == 0 and number != i:
                return False
        return True


while (tests > 0):
    n = int(input())
    prime_number = isPrime(n)
    if prime_number:
        print("Prime")
    else:
        print("Not prime")
    tests -= 1

