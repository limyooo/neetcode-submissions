class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n,m = len(grid),len(grid[0])
        dq = deque()
        fresh = 0
        minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while dq:
            infection = False
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            size = len(dq)
            for _ in range(size):
                x,y = dq.popleft()
                for i,j in direction:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        infection = True
                        dq.append((nx,ny))
            if infection:
                minutes += 1
        return minutes if fresh == 0 else -1
                