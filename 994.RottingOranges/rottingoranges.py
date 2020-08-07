class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        rotten = deque()
        time = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        while(rotten and fresh >= 1):
            time += 1
            n = len(rotten)
            while(n):
                curr_row, curr_col = rotten.popleft()
                for d in direction:
                    new_row = curr_row + d[0]
                    new_col = curr_col + d[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == 1:
                            fresh -= 1
                            rotten.append((new_row,new_col))
                            grid[new_row][new_col] = 2
                n -= 1

        if fresh > 0:
            return -1
        else:
            return time
