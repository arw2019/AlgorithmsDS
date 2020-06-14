class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                val = float('inf')
                if i>0: val = min(val, dp[i-1][j])
                if j>0: val = min(val, dp[i][j-1]) 
                dp[i][j] = grid[i][j] + (val if val < float('inf') else 0)
        return dp[-1][-1]
