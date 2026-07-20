class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n!=1 and n not in seen:
            seen.add(n)
            total = 0
            temp = n
            while temp > 0:
                a = temp % 10 
                total += a*a
                temp = temp // 10
            n = total
        return n == 1
                    

