#Simple solution
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    i = 0
    sumDiagonalL = 0
    for arrayL in arr:
        sumDiagonalL += arrayL[i]
        i += 1
    j = 0
    sumDiagonalR = 0
    for arrayR in arr:
        n = len(arrayR) - 1 
        sumDiagonalR += arrayR[n - j]
        j += 1
    return abs(sumDiagonalL - sumDiagonalR)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Optimized solution
def diagonalDifference(arr):
    # Write your code here
    i = 0
    sumDiagonalL = 0
    sumDiagonalR = 0
    for array in arr:
        n = len(array) - 1 
        sumDiagonalL += array[i]
        sumDiagonalR += array[n - i]
        i += 1
    return abs(sumDiagonalL - sumDiagonalR)