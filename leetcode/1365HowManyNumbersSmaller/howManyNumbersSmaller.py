# Solution: Brute force solution. Check each item and compare if it is smaller.
# Complexity: Time O(n^2) | Space O(n)
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = []
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if j != i and nums[j] < nums[i]:
                    count += 1
            smaller.append(count)
        return smaller

# Solution: Use of hash table. Copy list, sort list. Check how many elements are smaller than number[i] and store result in
# hash table. Do another iteration to display them in the original list order. 
# Complexity:  O(nlogn) | Space O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = []
        freq = {}
        sortedNums = nums.copy()
        sortedNums.sort()
        n = len(sortedNums)-1
        for i in range(n, -1, -1):
            freq[sortedNums[i]] = i
        for elem in nums:
            if elem in freq:
                smaller.append(freq[elem])
        return smaller