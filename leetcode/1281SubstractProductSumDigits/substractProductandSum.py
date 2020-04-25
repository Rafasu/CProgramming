class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productDigits = 1
        sumDigits = 0
        while n > 0:
            digit = n % 10
            productDigits *= digit
            sumDigits += digit
            n = n // 10
        return productDigits - sumDigits
            
        