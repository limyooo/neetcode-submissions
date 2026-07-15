class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        dq = deque()
        n,m = len(grid),len(grid[0])
        INF = 2147483647
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dq.append((i,j))
        
        while dq:
            x,y = dq.popleft()
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in direction:
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    dq.append((nx,ny))