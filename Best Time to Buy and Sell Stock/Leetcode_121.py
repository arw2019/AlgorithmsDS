class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSeen, curMax = 0, 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            curMax = max(curMax+diff, diff)
            maxSeen = max(maxSeen, curMax)
        return maxSeen
