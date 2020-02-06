# dynamic program 
# O(N) runtime

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot, ans = 0, nums[0] 
        for n in nums:
            tot += n
            ans = max(tot, ans)
            tot = max(tot, 0)
        return ans
    
# divide and conquer solution
# O(NlgN) runtime 
class Solution:
    
    def helper(self, nums, l, r):
        
        if  l >= r: 
            return float('-inf')
        
        mid = (l + r)//2
        
        # divide and recurse
        lMax = self.helper(nums, l, mid)
        rMax = self.helper(nums, mid+1, r)
        
        # compute maxSum of an array spanning left and right halves
        # this step is O(r-l)
        
        lCross, rCross = 0, 0
        tot = 0
        for i in range(mid-1, l-1, -1):
            tot += nums[i]
            lCross = max(lCross, tot)
                
        tot = 0
        for i in range(mid+1, r):
            tot += nums[i]
            rCross = max(rCross, tot)
        
        return max(lMax, rMax, lCross + nums[mid] + rCross)
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        return self.helper(nums, 0, len(nums))
        
