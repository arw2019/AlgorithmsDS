class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # this problem is a variation on the classic knapsack problem
        
        # Erik Demaine's five easy steps to DP
        # 1. subproblem = max no. strings that can be formed with i zeros and j ones 
        # 2. guessing: do we use i_th item or not
        # 3. recurrence
        # DP[i, j] = max(DP[i,j], 1+ DP[i - zi, n - o_i] if z_i < m and o_i < n)
        # 4. topological order: for s in strings for i in m...zeros(s) for j in n...ones(s)
        # 5. original problem: D[m, n]
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for s in strs:
            numZeros = s.count('0')
            numOnes = len(s) - numZeros
            if numZeros > m or numOnes > n: continue
            for i in range(m, numZeros-1, -1):
                for j in range(n, numOnes-1, -1):
                    dp[i][j] = max(dp[i][j], 1+ dp[i-numZeros][j-numOnes])
        
        return dp[m][n]
