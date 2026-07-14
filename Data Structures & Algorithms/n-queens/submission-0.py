class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n,0,res,chessboard)
        return res
    def backtracking(self,n,row,res,chessboard):
        if row == n:
            res.append(chessboard[:])
            return
        for col in range(n):
            if self.isvalid(col,row,chessboard,n):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracking(n,row+1,res,chessboard)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]

    def isvalid(self,col,row,chessboard,n):
        # col
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        # 45
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        #135:
        i,j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

