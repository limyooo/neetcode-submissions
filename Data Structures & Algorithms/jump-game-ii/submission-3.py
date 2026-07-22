class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        next_end = 0
        curr_end = 0
        n = len(nums)
        step = 0
        for i in range(n - 1):
            next_end = max(next_end,i + nums[i])
            if i == curr_end:
                step += 1
                curr_end = next_end
                if curr_end >= n - 1:
                    return step
                    