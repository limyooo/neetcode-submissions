class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        sq = [(index,i) for index,i in enumerate(queries)]
        sq.sort(key = lambda x:x[1])
        i = 0
        n = len(intervals)
        min_heap = []
        lens = 0
        res = [-1] * len(queries)
        for index,q in sq:
            while i < n and intervals[i][0] <= q:
                start,end = intervals[i]
                lens = end - start + 1
                heapq.heappush(min_heap,(lens,end))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                res[index] = min_heap[0][0]
            else:
                res[index] = -1
        return res 
