class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n,m = len(matrix),len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        def dfs(x,y):
            if dp[x][y] != 0:
                return dp[x][y]
            direction = [[1,0],[-1,0],[0,-1],[0,1]]
            path = 1
            curr_path = 0
            for i,j in direction:
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < m and matrix[x][y] < matrix[nx][ny]:
                    curr_path = dfs(nx,ny) + 1
                    path = max(path,curr_path)
            dp[x][y] = path
            return path
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res,dfs(i,j))
        return res

