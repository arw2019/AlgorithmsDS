class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        else:
            return mid + self.searchInsert(nums[mid:], target)
