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
            curr_pos = matrix[row][col]
            if curr_pos == target:
                return True
            if curr_pos > target:
                col -= 1
            elif curr_pos < target:
                row += 1
        return False
