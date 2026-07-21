class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        new = [0,0]
        n = len(intervals)
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            while i < n -1 and end >= intervals[i+1][0]:
                end = max(end,intervals[i+1][1])
                i += 1
            res.append([start,end])
            i += 1
        return res

