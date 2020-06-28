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
