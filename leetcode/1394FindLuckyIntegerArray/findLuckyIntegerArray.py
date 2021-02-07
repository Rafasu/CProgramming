# Solution: Build a frequency table, if key is equal to its frequency check if the lucky number is the maximum
# Complexity: Time O(n) | Space O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        luckyNumber = -1
        for key in freq:
            if(key == freq[key]):
                if(key > luckyNumber):
                    luckyNumber = key
        return luckyNumber