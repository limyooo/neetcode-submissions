class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m,n = len(num1),len(num2)
        res = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = (ord(num1[i])-48) * (ord(num2[j])-48)
                p1,p2 = i+j,i+j+1 #如果是两位数的话，p2就是当前该放的位置，p1就是十位进位的位置
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        ans = "".join(map(str,res)).lstrip('0')
        return ans