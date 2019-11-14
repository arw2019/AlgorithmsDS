# top 1%
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-2:i])
        return min(cost[-2:])
