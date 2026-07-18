class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        ans = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i + 1 <= 2:
                        dp[i][j] = True
                        ans += 1
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                            ans += 1
        return ans