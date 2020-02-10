import bisect
class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        nums.sort()
        for i, n in enumerate(nums):
            double = n*2
            if double <= nums[-1]:
                j = bisect.bisect_left(nums, double)
                if j!=i and 0<=j<len(nums) and nums[j]== double:
                    return True
        return False
