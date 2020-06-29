class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] += grid[i][j]
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                elif i > 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]

        return dp[len(dp)-1][len(dp[0])-1]
            
