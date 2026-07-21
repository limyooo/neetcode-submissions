class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        while x > 0 :
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        res *= sign
        if  res > 2 ** 31 - 1 or res < -2** 31 :
            return 0
        else:
            return res
