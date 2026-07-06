class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        index = 0
        for point in points:
            a,b = point
            dis = a*a + b*b
            heapq.heappush(max_heap,[- dis,index])
            index += 1
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [points[idx] for _, idx in max_heap]


