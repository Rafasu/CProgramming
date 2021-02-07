# Solution: Use a map to store the keys. Then find if i + 1 is a key
# Complexity: Time O(n) | Space O(1)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        freq = {}
        count = 0
        k = 0
        for num in arr:
            if(num not in freq):
                freq[num] = 1                
        for num in arr:
            k = num + 1
            if(k in freq):
                count += freq[k]
        return count
            