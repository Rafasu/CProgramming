# Solution: Count the number of digits for each numbers. Divide by 10 to get a new digit.
# Complexity:  Time O(n*m) | Space O(1)
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        evenNumbers = 0
        for i in range(n):
            number = nums[i]
            digits = 0
            while number > 0:
                digits += 1
                number = number // 10
            if(digits % 2 == 0):
                evenNumbers += 1
        return evenNumbers
        