class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        return nums.index(largest) if all(2 * x <= largest for x in nums if x != largest) else -1
