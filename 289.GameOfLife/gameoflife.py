class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        new_board = [[board[n][m] for m in range(m)] for n in range(n)]
        count = 0
        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for row in range(n):
            for col in range(m):
                count = 0
                for d in direction:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if 0 <= new_row < n and 0 <= new_col < m and new_board[new_row][new_col] == 1:
                            count += 1

                if new_board[row][col] == 1 and count < 2 or count > 3:
                    board[row][col] = 0
                if new_board[row][col] == 0 and count == 3:
                    board[row][col] = 1
