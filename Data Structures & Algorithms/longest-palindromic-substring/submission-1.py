class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) <= 1:
            return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        start = 0
        max_len = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j - i + 1 <= 2:
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start:start + max_len]
        

