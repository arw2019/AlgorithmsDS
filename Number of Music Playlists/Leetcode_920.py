import math
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        
        # Erik Demaine's five easy steps to DP
        # 1. subproblems: f(n, l; K)
        # 2. guessing: did we include all songs in L-1 songs
        # 3. recurrence
        # f(n, l; K) = N * f(n-1, l-1; K) + (n-K) * f(n, l-1; K)
        # 4. topological ordering of subproblems: for n in [K+1, N] for l in [i, L+1]
        # 5. answer to original problem: f(N, L, K)
        
        mod = 10**9 + 7
        dp = [[0 for _ in range(L+1)] for _ in range(N+1)]
        for n in range(K+1, N+1):
            for l in range(n, L+1):
                if n == l or l == K+1:
                    dp[n][l] = math.factorial(n) % mod
                else:
                    dp[n][l] = (dp[n-1][l-1]*n + dp[n][l-1]*(n-K)) % mod
        return dp[N][L]
