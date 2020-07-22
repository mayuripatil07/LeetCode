class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        i = 0
        res = []
        while(i < len(matrix)):
            min_value = math.inf
            max_value = -1
            flag = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] < min_value:
                    min_value = matrix[i][j]
                    row = i
                    col = j

            for k in range(len(matrix)):
                if matrix[row][col] < matrix[k][col]:
                    flag = 1
                    break
            if not flag:
                res.append(matrix[row][col])
            i += 1
        if not res:
            return []
        return res
