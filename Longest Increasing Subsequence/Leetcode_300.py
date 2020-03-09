# bottom-up DP
# O(N^2) time, O(N) space

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0 
        n = len(nums)
        dp = [1 for _ in range(n)]
        # dp[i] = length of longest subsequence beginning at index i
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
