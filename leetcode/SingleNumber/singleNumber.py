# Solution: Building a freq table
# Complexity: Time  O(n) | Space O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = {}
        for i in range(len(nums)):
            if(nums[i] in frequency):
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
                
        for key in frequency:
            if(frequency[key] == 1):
                return key

# Solution: Delete repeated values
# Complexity: Time O(n) | Space O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setN = {}
        for i in range(len(nums)):
            if(nums[i] in setN):
                del setN[nums[i]]
            else:
                setN[nums[i]] = 1
        for key in setN:
            return key

# Same way as above but different return
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setN = {}
        for i in range(len(nums)):
            if(nums[i] in setN):
                del setN[nums[i]]
            else:
                setN[nums[i]] = 1
        return list(setN.keys())[0]

# Using Set
# Complexity: Time O(n) | Space O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

#Biwide XOR
#Complexity: Time O(n) | Space O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res