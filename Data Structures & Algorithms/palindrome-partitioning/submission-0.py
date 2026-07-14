class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s,0,[],res)
        return res
    def is_palindrome(self,s,start,end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def backtracking(self,s,index,path,res):
        if index == len(s):
            res.append(path[:])
        for i in range(index,len(s)):
            if self.is_palindrome(s,index,i):
                path.append(s[index:i+1])
                self.backtracking(s,i+1,path,res)
                path.pop()

