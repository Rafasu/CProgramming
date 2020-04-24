# Solution: Using dictionary
# Complexity:  Time O(n) | Space O(m)
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}
        for char in J:
            jewels[char] = 1
        
        n = len(S)
        count = 0
        for i in range(n):
            if( S[i] in jewels):
                count += 1
        return count 
# Solution: Using set. This is more legible.
# Complexity:  Time O(n) | Space O(m)
class Solution(object):
    def numJewelsInStones(self, J, S):
        jewels = set(J)
        count = 0
        for char in S:
            if( char in jewels):
                count += 1
        return count 