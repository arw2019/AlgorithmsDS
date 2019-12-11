class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        def isBigger(x: int) -> bool:
            """finds whether nums contains a subarray with average >= x in O(N) time"""
            cur = sum([nums[i] - x for i in range(k)])
            if cur > 0: return True
            prev, prevSmallest = 0, 0
            for i in range(k, len(nums)):
                cur += (nums[i] - x)
                prev += (nums[i-k] - x)
                prevSmallest = min(prev, prevSmallest)
                if cur >= prevSmallest: return True
            return False
        
        # binary search on the result using isBigger for the compare function
        # isBinary takes  O(N) time => total time complexity is O(NlgN)
        lo, hi = min(nums), max(nums)    
        while hi - lo >= 1e-5:
            mid = (lo+hi)/2.
            if isBigger(mid): lo = mid
            else: hi = mid      
        return lo

# brute force solution
# O(N^2) time
# TLE
class Solution:
    def helper(self, nums: List[int], k: int) -> float:
        if k == 0: return float('-inf')
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums))/k
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return max(self.helper(nums, x) for x in range(k, len(nums)+1))
