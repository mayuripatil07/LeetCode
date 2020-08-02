class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    count = max(self.dfs(i,j,grid), count)

        return count

    def dfs(self,i,j,grid):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        up = self.dfs(i,j+1,grid)
        down = self.dfs(i,j-1,grid)
        left = self.dfs(i-1,j,grid)
        right = self.dfs(i+1,j,grid)

        return up + down + left + right + 1
