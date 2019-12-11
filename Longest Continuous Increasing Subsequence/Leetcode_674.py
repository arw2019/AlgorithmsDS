class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        curLen, maxLen = 1, 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 0:
                curLen += 1
            else: 
                curLen, maxLen = 1, max(maxLen, curLen)
        return max(maxLen, curLen)
