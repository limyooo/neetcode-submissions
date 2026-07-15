class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        self.visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    if self.dfs(board,word,i,j,0):
                        return True
        return False
        
    def dfs(self,board,word,x,y,index):
        if board[x][y] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        self.visited[x][y] = True
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        for i,j in direction:
            nx = x + i
            ny = y + j
            if  0 <= nx < len(board) and 0 <= ny < len(board[0]) and not self.visited[nx][ny]:
                if self.dfs(board,word,nx,ny,index + 1):
                    return True
        self.visited[x][y] = False
        return False

