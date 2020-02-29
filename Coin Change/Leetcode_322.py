# knapsack problem
# solution O(nS) where n=number of denominations, S=target amount

class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        dp = [0] + [float('inf') for _ in range(target)]
        for amount in range(1, target+1):
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], dp[amount-coin]+1)
        return -1 if dp[-1]==float('inf') else dp[-1]                 
