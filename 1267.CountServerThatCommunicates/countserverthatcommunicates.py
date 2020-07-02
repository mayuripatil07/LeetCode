class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        flag  = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for row in range(0,m):
                        if row == j:
                            continue
                        else:
                            if grid[i][row] == 1:
                                count += 1
                                flag = 1
                                break
                    if not flag:
                        for col in range(0,n):
                            if col == i:
                                continue
                            else:
                                if grid[col][j] == 1:
                                    count += 1
                                    break
                    flag = 0

        return count
