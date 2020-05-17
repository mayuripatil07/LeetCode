class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        self.found = False
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    temp = board[row][col]
                    board[row][col] = "#"
                    self.dfs(board, word, row, col, 1)
                    board[row][col] = temp

        return self.found


    def dfs(self, board, word, row, col, index):
        directions = [(-1,0), (0,1),(1,0),(0,-1)]
        if not self.found:
            if index == len(word):
                self.found = True
                return
            else:
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if (0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] != "#"):
                        if board[new_row][new_col] == word[index]:
                            temp = board[new_row][new_col]
                            board[new_row][new_col] = "#"
                            self.dfs(board, word, new_row, new_col, index+1)
                            board[new_row][new_col] = temp



        
