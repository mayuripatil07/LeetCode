class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def cell(cells):
            masks = cells.copy()
            for i in range(1,7):
                if masks[i-1] == masks[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0

            cells[0] = 0
            cells[-1] = 0
            return cells


        day1 = tuple(cell(cells))
        N -= 1
        count = 0

        while(N > 0):
            day = tuple(cell(cells))
            N -= 1
            count += 1

            if day == day1:
                N = N % count

        return cells
            
