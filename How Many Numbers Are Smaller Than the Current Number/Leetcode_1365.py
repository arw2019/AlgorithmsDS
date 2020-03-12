from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        return [bisect_left(sortedNums, num) for num in nums]
