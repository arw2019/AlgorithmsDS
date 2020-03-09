# O(NlgN) solution
# O(L) space where L is the length of LIS
# so also can say O(N) space

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ISS = []
        for n in nums:
            insertPos = bisect_left(ISS, n)
            if insertPos == len(ISS):
                ISS += [n]
            else:
                ISS[insertPos] = n
        return len(ISS)

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
