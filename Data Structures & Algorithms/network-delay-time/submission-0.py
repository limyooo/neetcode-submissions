class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_distance = [float('inf')] * (n+1)
        visited = [False] * (n+1)
        min_distance[k] = 0
        grid = [[float('inf')] * (n+1) for _ in range(n+1)]
        for u,v,t in times:
            grid[u][v] = t
        for i in range(1,n+1):
            cur = -1
            min_val = float('inf')
            for j in range(1,n+1):
                if visited[j] == False and min_distance[j] < min_val:
                    min_val = min_distance[j]
                    cur = j
        
            if min_val == float('inf'):
                break
            visited[cur] = True
            for j in range(1,n+1):
                if not visited[j]:
                    min_sum = min_val + grid[cur][j]
                    if min_distance[j] > min_sum:
                        min_distance[j] = min_sum
        ans = max(min_distance[i] for i in range(1,n+1))
        if ans == float('inf'):
            return -1
        else:
            return ans 






