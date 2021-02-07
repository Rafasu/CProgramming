# Solution: Using Set. If we multiply a set by 3, and substract the given array of numbers
# We will get as a residual 2(i) where i is the unique number, if we divide by two that residual
# we will get the unique number
# Complexity: Time O(n) | Space O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums))//2


# You can also solve this with a frequency hash table or bitwise operations
        