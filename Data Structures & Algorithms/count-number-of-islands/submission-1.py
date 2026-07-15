class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        count = 0
        visited = [[False] * m for _ in range(n)]

        def dfs(x,y):
            visited[x][y] = True
            if grid[x][y] == '0':
                return
            direction = [[1,0],[-1,0],[0,-1],[0,1]]
            for i,j in direction:
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    dfs(nx,ny)
                
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j)
                    
        return count
    
            