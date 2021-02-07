# Solution: No use of python built in functions.
# Complexity:  Time O(n) | Space O(n)
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defang = ''
        n = len(address)
        for i in range(n):
            if(address[i] == '.'):
                defang += '[.]'
            else:
                defang += address[i]
        return defang
# Solution 2 and 3: Use of python built in functions
# Complexity: Time O(n) | Space O(1)
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')
# Separate them by the period in an array. Join in a string with [.] between.
class Solution(object):
    def defangIPaddr(self, address):
        return "[.]".join(address.split("."))

        