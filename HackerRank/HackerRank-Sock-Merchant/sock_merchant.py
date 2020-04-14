# Solution: Use hash table to stro freq of numbers and then add pairs to variable
# Complexity: Time O(n) | Space O(n)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq = {}
    for i in range(n):
        if(ar[i] in freq):
            freq[ar[i]] += 1
        else:
            freq[ar[i]] = 1
    pairs = 0
    for elem in freq:
        if( freq[elem] >= 2):
            pairs += (freq[elem]//2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
