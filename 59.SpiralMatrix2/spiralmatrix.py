class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        x = 0
        y = 0
        val = 1
        while(n):
            if n == 1:
                result[x][y] = val
                break
            #left to right
            for i in range(n-1):
                result[x][y] = val
                y += 1
                val += 1
            #top to bottom
            for i in range(n-1):
                result[x][y] = val
                x += 1
                val += 1
            #right to left
            for i in range(n-1):
                result[x][y] = val
                y -= 1
                val+= 1
            #bottom to top
            for i in range(n-1):
                result[x][y] = val
                x -= 1
                val += 1

            x += 1
            y += 1
            n -= 2
        return result
