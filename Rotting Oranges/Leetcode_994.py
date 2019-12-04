class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue, clock = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 2], 0
        while queue:
            nextTimestep = []
            for i, j in queue:
                for k, l in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=k<m and 0<=l<n and grid[k][l] == 1:
                        nextTimestep += [(k,l)]
                        grid[k][l] = 2
            if not nextTimestep: break
            queue = nextTimestep
            clock+=1
                       
        return -1 if any([grid[i][j] == 1 for i in range(m) for j in range(n)]) else clock