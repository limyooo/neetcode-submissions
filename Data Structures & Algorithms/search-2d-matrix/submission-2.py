class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left  = 0
        right = len(matrix) * len(matrix[0]) - 1
        if not matrix or not matrix[0]:
            return False
        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
            
