class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)-1
        while nums[lo] + nums[hi] != target:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                lo += 1
        return [lo+1, hi+1]
