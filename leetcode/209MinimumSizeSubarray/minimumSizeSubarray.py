# Solution: Sliding window pattern using two pointers.
# Complexity: Time O(n) | Space O(1)

import math
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        window_sum = 0
        min_length = math.inf
        window_start = 0
        n = len(nums)
        
        for window_end in range(n):
            window_sum += nums[window_end]
            
            while(window_sum >= s):
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1    
        if(min_length == math.inf):
            return 0
        return min_length
                