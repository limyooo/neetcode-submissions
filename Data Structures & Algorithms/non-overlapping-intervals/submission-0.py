class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        i = 0
        while i < n:
            end = intervals[i][1]
            while i < n - 1 and end > intervals[i+1][0]:
                count += 1
                i += 1
            i += 1
        return count