# Complexity:  Time O(n) | Space O(1)
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        l = 0
        count = 0
        for char in s:
            if(char == 'L'):
                l += 1
            else:
                r += 1
            if r == l:
                count += 1
                r = 0
                l = 0
        return count
        