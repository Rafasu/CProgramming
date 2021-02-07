# Solution: Two pass Hash Table
# Complexity: Time O(n) | Space O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            complements[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in complements and i != complements[complement]):
                return [i, complements[complement]]
        
        return []

# Solution: One Pass Hash Table
# Complexity: Time O(n) | Space O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [i, complements[complement]]
            complements[num] = i
        return 