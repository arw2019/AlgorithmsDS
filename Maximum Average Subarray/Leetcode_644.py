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
