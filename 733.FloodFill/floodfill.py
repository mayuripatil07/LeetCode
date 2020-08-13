class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [(sr,sc)]
        seen = set()
        original_color = image[sr][sc]
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        while(stack):
            row, col = stack.pop()
            for d in direction:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                    if image[new_row][new_col] == original_color and (new_row, new_col) not in seen:
                        stack.append((new_row, new_col))
            image[row][col] = newColor
            if (row,col) not in seen:
                seen.add((row, col))
        return image
