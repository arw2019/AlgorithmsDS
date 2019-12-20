class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        digits_1_to_9 = set(range(1,10))
        for i in range(m-2):
            for j in range(n-2):
                digits_in_square = set([grid[i+I][j+J] for I in range(3) for J in range(3)])
                if digits_in_square == digits_1_to_9:
                    row_sums = [sum(grid[i+I][j+J] for J in range(3)) for I in range(3)]
                    col_sums = [sum(grid[i+I][j+J] for I in range(3)) for J in range(3)]
                    diag_sum = [sum(grid[i+x][j+x] for x in range(3))]
                    anti_diag_sum = [sum(grid[i+x][j+x] for x in range(3))]
                    unique_sums = set(row_sums + col_sums + diag_sum +anti_diag_sum)
                    if len(unique_sums)  == 1: ans +=1
        return ans
