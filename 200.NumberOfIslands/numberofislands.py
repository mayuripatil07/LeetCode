class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i , j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, row, col):
        grid[row][col] = '0'
        direction = [(0,1),(0,-1),(-1,0),(1,0)]
        for d in direction:
            new_row = row + d[0]
            new_col = col + d[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                self.dfs(grid, new_row, new_col)
