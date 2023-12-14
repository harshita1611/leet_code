class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(rows)) for j in range(cols)]

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            ones_row = row_sums[i]
            zeros_row = cols - ones_row

            for j in range(cols):
                ones_col = col_sums[j]
                zeros_col = rows - ones_col

                ans[i][j] = ones_row - zeros_row + ones_col - zeros_col

        return ans
