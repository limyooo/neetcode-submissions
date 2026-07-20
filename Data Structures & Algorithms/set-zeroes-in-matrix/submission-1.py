class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        row_0 = False
        col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                col_0 = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for i in range(m):
            if row_0:
                matrix[i][0] = 0
        for j in range(n):
            if col_0:
                matrix[0][j] = 0
