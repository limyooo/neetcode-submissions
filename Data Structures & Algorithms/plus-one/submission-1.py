class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = num * 10 + i
        total = num + 1

        res = []
        while total > 0:
            a = total % 10 
            res.append(a)
            total = total // 10
        
        res.reverse()
        return res

        