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
