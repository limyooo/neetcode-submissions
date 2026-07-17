class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_distance = [float('inf')] * (n+1)
        min_distance[k] = 0
        grid = defaultdict(list)
        for u,v,t in times:
            grid[u].append((v,t))
        
        min_heap = [(0,k)]
        while min_heap:
            time,node = heapq.heappop(min_heap)
            if time > min_distance[node]:
                continue
            for next_node,dist in grid[node]:
                new_distance = time + dist
                if new_distance < min_distance[next_node]:
                    min_distance[next_node] = new_distance
                    heapq.heappush(min_heap,(new_distance,next_node))
        ans = max(min_distance[1:])
        return ans if ans != float('inf') else -1
