class Solution:

    def calculateMinimumHP(self, dungeon: 'List[List[int]]') -> int:

        if not (dungeon and dungeon[0]): return 0
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m][n-1], dp[m-1][n] = 1, 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need
        
        return dp[0][0]


s = Solution()
input_1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]] 
result_1 = s.calculateMinimumHP(input_1)
print(f'Input = {input_1}; result = {result_1}')
input_2 = [[-2,-3,3]] 
result_2 = s.calculateMinimumHP(input_2)
print(f'Input = {input_2}; result = {result_2}')

