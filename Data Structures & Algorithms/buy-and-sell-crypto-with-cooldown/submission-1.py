class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -prices[0]
        sold = 0
        unhold = 0
        for i in range(1,n):
            pre_hold = hold
            pre_sold = sold
            pre_unhold = unhold
            hold = max(pre_hold,pre_unhold - prices[i])
            sold = pre_hold + prices[i]
            unhold = max(pre_sold,pre_unhold)
        return max(sold,unhold)