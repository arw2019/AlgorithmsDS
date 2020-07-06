class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        try:
            m, n = len(matrix), len(matrix[0])
        except IndexError:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxSideLength = 0
        
        for i in range(m):
            for j in range(n):
                if i ==0 or j ==0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                maxSideLength = max(maxSideLength, dp[i][j])
                
        return maxSideLength**2
