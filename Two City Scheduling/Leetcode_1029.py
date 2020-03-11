class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mid = len(costs)//2
        costs.sort(key = lambda x: x[0]-x[1])
        return sum(c for c, _ in costs[:mid]) + sum(c for _, c in costs[mid:])
