class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        queue = deque()
        length = 0
        visited = set()
        queue.append((0,0))
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while(queue):
            length += 1
            n = len(queue)
            while(n):
                x , y = queue.popleft()
                if x == len(grid)- 1 and y == len(grid[0]) - 1:
                    return length
                for d in direction:
                    new_row = x + d[0]
                    new_col = y + d[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited:
                        if grid[new_row][new_col] == 0:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
                n -= 1
        return -1
