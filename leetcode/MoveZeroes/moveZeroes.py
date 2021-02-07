# Solution: A solution will be to store an array/vector to store all the numbers
# that are different from zero, after that you just fill the before or after it with 
# the missing zeros.
# Because this is a problem that requires to make it without extra memory you will need to 
# Use a pointer, this pointer for this specific problem is point to the the beginning of the
# array. Because there you will fill it with the numbers different from zero. After that follow same
# Approach as mentioned above.
# Complexity:  Time O(n) | Space O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nxt = 0
        for i in range(n):
            if(nums[i] != 0):
                nums[nxt] = nums[i]
                nxt += 1
        for j in range(nxt, n):
            nums[j] = 0