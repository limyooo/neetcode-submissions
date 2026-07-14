class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(start,path,total):
            if total > target:
                return
            if total == target:
                res.append(path[:])
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                total += candidates[i]
                path.append(candidates[i])
                backtracking(i+1,path,total)
                total -= candidates[i]
                path.pop()
        backtracking(0,[],0)
        return res