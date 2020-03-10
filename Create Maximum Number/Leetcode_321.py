class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if not (nums1 or nums2): return []
        
        m, n, res = len(nums1), len(nums2), []
        dp1, dp2 = self.maxArray(nums1, m), self.maxArray(nums2, n)
        
        for i in range(min(m+1, k+1)):
            if k-i not in dp2:
                continue
            res = max(res, [(max(dp1[i], dp2[k-i])).pop(0) for _ in range(k)])
 
        return res
    
    def maxArray(self, nums: List[int], length: int):
        dp = {length: nums}
        i = 0
        while length:
            while i+1<length and nums[i]>=nums[i+1]:
                i+=1
            nums = nums[:i]+ nums[i+1:]
            length -=1
            dp[length] = nums
            if i > 0: i-=1
        return dp
