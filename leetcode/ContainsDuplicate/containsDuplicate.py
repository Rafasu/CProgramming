# Solution: Using a HashTable to store a frequency table.
# Complexity: Time: O(n) Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        for i in range(len(nums)):
            if nums[i] in countDict:
                countDict[nums[i]] += 1
            else:
                countDict[nums[i]] = 1
        for key in countDict:
            if countDict[key] > 1:
                return True

# Runtime: 136 ms, faster than 25.43% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20 MB, less than 7.55% of Python3 online submissions for Contains Duplicate.

# Solution: Using a Hash Table an returning true if the value is already in there
# Complexity: Time: O(n) Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        for i in range(len(nums)):
            if nums[i] in countDict:
                return True
            else:
                countDict[nums[i]] = 1
        return False
# Runtime: 132 ms, faster than 44.17% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19.2 MB, less than 16.98% of Python3 online submissions for Contains Duplicate.


# Solution: Using set 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) > len(set(nums)))

# Runtime: 116 ms, faster than 97.91% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.3 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
