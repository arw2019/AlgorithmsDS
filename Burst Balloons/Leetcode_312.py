# pythonized DP solution

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        
        dp = [[0 for _ in range(N+2)] for _ in range(N+2)]
        
        for length in range(1, N+1):
            for start in range(1, N-length+2):
                end = start + length -1
                dp[start][end] = max( 
                        dp[start][final-1] +
                        nums[start-1]*nums[final]*nums[end+1] +
                        dp[final+1][end]
                        for final in range(start, end+1)
                ) 
    
        return dp[1][N]

# DP solution
# subproblem: best score for subarray nums[start:end]
# O(N^3) time, O(N^2) space

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        
        dp = [[0 for _ in range(N+2)] for _ in range(N+2)]
        
        for length in range(1, N+1):
            for start in range(1, N-length+2):
                end = start + length -1
                bestCoins = 0
                for final in range(start, end+1):
                    coins = ( 
                        dp[start][final-1] +
                        nums[start-1]*nums[final]*nums[end+1] +
                        dp[final+1][end]
                    ) 
                    if coins > bestCoins: bestCoins = coins
                dp[start][end] = bestCoins
    
        return dp[1][N]
    
# brute force recursion
# O(N!) runtime
# TLE - obviously

from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize=None) 
        def recurse(nums):
            if not nums: 
                return 0 
            elif len(nums) == 1: 
                return nums[0]
            elif len(nums) == 2:
                return nums[0]*nums[1] + max(nums)
            else:
                res = float('-inf')
                res = max(res, nums[0]*nums[1] + self.maxCoins(nums[1:]))
                for i in range(1, len(nums)-1):
                    res = max(res, 
                            nums[i-1]*nums[i]*nums[i+1] + 
                            self.maxCoins(nums[:i]+nums[i+1:])
                            )
                    res = max(res, self.maxCoins(nums[:-1]) + nums[-2]*nums[-1])
            return res
        
        return recurse(tuple(nums))
