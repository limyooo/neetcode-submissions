class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        visited = [False] * n
        ans = 0
        for _ in range(n):
            curr = -1
            min_val = float('inf')
            for i in range(n):
                if min_val > min_cost[i] and not visited[i]:
                    min_val = min_cost[i]
                    curr = i
            visited[curr] = True
            ans += min_val
            for j in range(n):
                if not visited[j]:
                    new_cost = abs(points[curr][0] - points[j][0]) + abs(points[curr][1] - points[j][1])
                    if min_cost[j] > new_cost:
                        min_cost[j] = new_cost
        return ans
