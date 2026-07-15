class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n,m = len(grid),len(grid[0])
        visited = [[False] * m for _ in range(n)]
        max_area = 0
        def dfs(x,y):
            if grid[x][y] == 0:
                return 0
            curr_area = 1
            visited[x][y] = True
            direction = [[1,0],[-1,0],[0,-1],[0,1]]
            for i,j in direction:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    curr_area += dfs(nx,ny)
            return curr_area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area,dfs(i,j))
        return max_area