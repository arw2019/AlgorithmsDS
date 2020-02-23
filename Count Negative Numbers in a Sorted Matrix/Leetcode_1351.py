class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not (grid and grid[0]): return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for row in grid:
            j = n-1
            while j >= 0 and row[j] < 0:
                ans += 1
                j-=1
        return ans
