class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0] 持有股票的profit，dp[i][1]不持有股票的(今天刚卖出去cooldown)profit,dp[i][2]不持有股票可以买入
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0]+prices[i]
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
        return max(dp[-1][1],dp[-1][2])