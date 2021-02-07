#Solution: Change number to binary representation. Then check the number of consecutive 1's
# Complexity: Time O(n * c) | Space O(c)

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    representation = ''
    while (n > 0 ):
        bit  = n % 2
        representation = str(bit) + representation
        n = n // 2
    consecutive = 0
    current = 0
    for char in representation:
        if(char == '1'):
            current += 1
            if(current >= consecutive):
                consecutive = current
        else: 
            current = 0
    print (consecutive)
