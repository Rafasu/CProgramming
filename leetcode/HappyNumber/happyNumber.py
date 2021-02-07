# Solution: Using set, you can use a dict/Map to but a set is more practical-easy to read
# Store the new numbers, to check if there's a cycle, otherwise it will repeat forever.
# Complexity: Time O(n) | Space O(m)
class Solution:
    def isHappy(self, n):
        mem = set()
        while n != 1:
            sumN = 0
            for i in str(n):
                sumN += int(i) ** 2 
            n = sumN
            if n in mem:
                return False
            else:
                mem.add(n)
    
        return True
            
        