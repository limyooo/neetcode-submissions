class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target:
            return 0
        if (total + target) % 2 != 0:
            return 0
        need = (total + target) // 2
        dp = [0] * (need + 1)
        dp[0] = 1
        for num in nums:
            for i in range(need,num - 1,-1):
                dp[i] += dp[i - num]
        return dp[need]

        