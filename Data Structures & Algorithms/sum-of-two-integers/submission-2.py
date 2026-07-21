class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF
        while b!= 0:
            digit = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = digit
            b = carry
        return a if a < 0x7FFFFFF else ~(a ^ mask)