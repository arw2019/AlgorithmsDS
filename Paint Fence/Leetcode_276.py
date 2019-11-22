class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n == 1: return k
        dp = [0]*(n+1)
        dp[1], dp[2] = k, k*k
        for i in range(3,n+1):
            dp[i] = (dp[i-2] + dp[i-1]) * (k-1)
        return dp[-1]