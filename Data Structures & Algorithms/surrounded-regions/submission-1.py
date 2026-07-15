class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 
        n,m = len(board),len(board[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(x,y):
            visited[x][y] = True
            direction = [[1,0],[-1,0],[0,1],[0,-1]]

            for i,j in direction:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if board[nx][ny] == 'O':
                        dfs(nx,ny)

        
        for i in range(n):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i,0)
            if board[i][m-1] == 'O' and not visited[i][m-1]:
                dfs(i,m-1)
        
        for j in range(m):
            if board[0][j] == 'O' and not visited[0][j]:
                dfs(0,j)
            if board[n-1][j] == 'O' and not visited[n-1][j]:
                dfs(n-1,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'




