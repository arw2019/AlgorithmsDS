class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        i = 1
        while i<len(nums) and cnt <= 1:
            if nums[i-1]>nums[i]:
                cnt+=1
                if i<2 or (nums[i-2] <= nums[i]):
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            i+=1 
        return cnt <= 1
