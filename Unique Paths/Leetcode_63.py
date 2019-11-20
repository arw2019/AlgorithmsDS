# top 4%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        self.memo = {}
        self.memo[0,0] = 1*(obstacleGrid[0][0] == 0)
        def numberOfPaths(i: int, j: int) -> int:
            if i < 0 or j < 0: return 0
            if (i, j) not in self.memo:
                if obstacleGrid[i][j] == 1: 
                    self.memo[i,j] = 0
                else:
                    self.memo[i,j] = numberOfPaths(i-1,j) + numberOfPaths(i, j-1)
            return self.memo[i,j]
        return numberOfPaths(m-1, n-1)
