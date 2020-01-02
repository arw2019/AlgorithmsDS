class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.islands = 0
        
        def dfs(i: int, j: int) -> None:
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '#'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        if grid:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        self.islands += 1
                        dfs(i, j)
        
        
        return self.islands
