# bottom-up DP
#  O(N^3) time, O(N^2) space
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        N = len(cuts)
       
        dp = [[0]*N for _ in range(N)] 
        
        for s in range(2, N):
            for i in range(N-s):
                dp[i][i+s] = min((
                    dp[i][k] + dp[k][i+s] 
                    for k in range(i+1, i+s)
                ))  + cuts[i+s] - cuts[i]
  
        return dp[0][-1]

# top-down DP
# recursive solution with caching
# still O(N!) complexity but much faster b/c caching

from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort() 
        
        @lru_cache(maxsize=None)
        def helper(n, cuts): 
            if len(cuts) == 0:
                minCost = 0
            elif len(cuts) == 1:
                minCost=n
            else:
                minCost = float('inf')
                for i in range(len(cuts)):
                    minCost = min(
                        minCost, 
                        n + helper(cuts[i], tuple(cuts[:i])) + \
                        helper(n-cuts[i], tuple(c - cuts[i] for c in cuts[i+1:])))
                
            return minCost
        
        return helper(n, tuple(cuts))

# recursive solution
# O(N!) time complexity, N=len(cuts)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort() 
        
        # dp(i, j) = min cost of cut between cuts[i] & cuts[j] non-inclusive
        # base case: dp(i, i+1) = 0
        # recursion: dp(i, j) = min_cost (all possible cuts i:j)
        
        if len(cuts) == 0:
            minCost = 0
        elif len(cuts) == 1:
            minCost=n
        else:
            minCost = float('inf')
            for i in range(len(cuts)):
                minCost = min(
                    minCost, 
                    n + self.minCost(cuts[i], cuts[:i]) + \
                    self.minCost(n-cuts[i], [c - cuts[i] for c in cuts[i+1:]]))
                
        return minCost
