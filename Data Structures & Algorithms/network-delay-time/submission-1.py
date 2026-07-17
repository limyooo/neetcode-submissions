from _heapq import heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        min_dis = [float('inf')] * (n+1)
        min_dis[k] = 0
        for u,v,t in times:
            graph[u].append((v,t))
        
        min_heap = [(0,k)]
        while min_heap:
            dist,curr = heapq.heappop(min_heap)
            if dist > min_dis[curr]:
                continue
            for nei,time in graph[curr]:
                new_dist = dist + time
                if new_dist < min_dis[nei]:
                    min_dis[nei] = new_dist
                    heapq.heappush(min_heap,(new_dist,nei))
        ans = max(min_dis[1:])
        return ans if ans != float('inf') else -1

