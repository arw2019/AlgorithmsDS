# recursive solution
# O(N!) time complexity, N=len(cuts)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort() 
        # print(f"n={n}, cuts={cuts}")
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
