# same DP solution
# but optimized to constant space

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        cost0, cost1, cost2 = 0, 0, 0
        for row in costs:
            cost0, cost1, cost2 = \
            row[0] + min(cost1, cost2), \
            row[1] + min(cost0, cost2), \
            row[2] + min(cost0, cost1)
        return min(cost0, cost1, cost2)

# DP solution
# O(N) time, O(N) space
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        n = len(costs)
        for i in range(1,n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])
