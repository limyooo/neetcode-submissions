class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtracking(0,digits)
        return self.res
    
    def __init__(self):
        self.letterMap = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'

        ]
        self.res = []
        self.s = ''
    def backtracking(self,index,digits):
        if index == len(digits):
            self.res.append(self.s)
            return 
        digit = int(digits[index])
        letter = self.letterMap[digit]
        for i in range(len(letter)):
            self.s += letter[i]
            self.backtracking(index+1,digits)
            self.s = self.s[:-1]
        


