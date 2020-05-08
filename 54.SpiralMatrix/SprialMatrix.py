class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while(matrix and matrix[0]):
            if matrix[0]:
                result += matrix.pop(0)

            if matrix:
                for last in matrix:
                    result.append(last.pop())

            if matrix and matrix[-1]:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for first in matrix[::-1]:
                    result.append(first.pop(0))

        return result
