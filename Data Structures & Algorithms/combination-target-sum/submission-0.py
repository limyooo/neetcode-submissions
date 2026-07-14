class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(start,path,total):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(start,len(nums)):
                total += nums[i]
                path.append(nums[i])
                backtracking(i,path,total)
                total -= nums[i]
                path.pop()
        backtracking(0,[],0)
        return res