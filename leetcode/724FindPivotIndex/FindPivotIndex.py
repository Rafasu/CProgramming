# Solution: My First solution was to use to arrays to calculate left and right sums but then I figured out
# that we can calculate leftsum and rightsum with the total sum and substracting each side values
# Complexity: Time O(n) | Space O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        n  = len(nums)
        
        for i in range(n):
            if(leftSum == total - leftSum - nums[i]):
                return i
            leftSum = leftSum + nums[i]

        return -1

# Same approach as above.
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum  = 0
        rightSum = sum(nums)
        n = len(nums)
        
        for i in range(n):
            rightSum = rightSum - nums[i]
            if(leftSum  == rightSum):
                return i
            leftSum = leftSum + nums[i]
        return -1