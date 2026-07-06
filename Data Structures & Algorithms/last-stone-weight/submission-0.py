class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while max_heap:
            if len(max_heap) == 1:
                return - max_heap[0]
            a = - heapq.heappop(max_heap)
            b = - heapq.heappop(max_heap)
            ans = abs(a-b)
            heapq.heappush(max_heap,- ans)
        
        return 0

