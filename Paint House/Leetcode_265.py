class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not (costs and costs[0]): return 0
        n, k = len(costs), len(costs[0])
        
        min1, min2, minColor = 0, 0, -1
        for _, row in enumerate(costs):
            curMin1, curMin2, curMinColor = float('inf'), float('inf'), 0
            for color, cost in enumerate(row):
                netCost = cost + (min2 if color==minColor else min1)
                if netCost < curMin1:
                    curMin1, curMin2, curMinColor = netCost, curMin1, color
                elif netCost < curMin2:
                    curMin2 = netCost
            min1, min2, minColor = curMin1, curMin2, curMinColor
    
        return min1
