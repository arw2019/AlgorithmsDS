# top 1.5%
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> int:
            if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                area = 1
                grid[i][j] = -1
                area += sum([dfs(i+1, j), dfs(i-1, j), dfs(i, j-1), dfs(i, j+1)])
                return area
            return 0
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        
        return ans
