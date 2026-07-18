class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        #dp[i] 表示前i个字符是否可以拆分成字典单词
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
