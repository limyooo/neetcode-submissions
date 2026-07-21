class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF
        while b:
            bit = (a ^ b) & mask 
            carry = ((a & b) << 1) & mask
            a = bit
            b = carry
        return a if a <= 0x7FFFFFF else ~(a^mask)