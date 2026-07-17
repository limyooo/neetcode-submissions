class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        min_heap = [(grid[0][0],0,0)]
        while min_heap:
            water,x,y = heapq.heappop(min_heap)
            if x == n - 1 and y == n - 1:
                return water
            direction = [[1,0],[-1,0],[0,-1],[0,1]]
            for i,j in direction:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < n:
                    new_water = max(water,grid[nx][ny])
                    if new_water < dist[nx][ny]:
                        dist[nx][ny] = new_water
                        heapq.heappush(min_heap,(new_water,nx,ny))
        return -1