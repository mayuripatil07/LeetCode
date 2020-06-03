 class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while(row < len(matrix) and col >=0):
            curr_val = matrix[row][col]
            if curr_val == target:
                return True
            if curr_val < target:
                row += 1
            if curr_val > target:
                col -= 1
        return False
        
