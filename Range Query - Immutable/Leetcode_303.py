# completely brute force with caching
# AC

from functools import lru_cache

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    @lru_cache()
    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
