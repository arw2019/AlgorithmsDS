class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        
        for i, n in enumerate(nums):
            if i <= end:
                end = max(end, i+n)
            else:
                return False
       
        return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ranges = []
        
        for i, n in enumerate(nums):
            if ranges and i <= ranges[-1][1]:
                ranges[-1][1] = max(ranges[-1][1], i+n)
            else:
                ranges += [[i, i+n]]
        
        return ranges[0][-1]>=len(nums)-1
