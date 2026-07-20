class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        num = 1.0
        while n > 0:
            if n % 2 != 0:
                num *= x
            
            x *= x
            n //= 2
        return num


