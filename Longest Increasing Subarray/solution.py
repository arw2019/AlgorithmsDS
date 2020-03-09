class Solution:
    def lengthOfLISubarray(self, nums: List[int]) -> int:
        """
        subproblem dp(i): length of longest increasing subsequence ending at index i-1
        guessing: is nums[i] part of the subsequence or is it the start of a new one?
        recurrence relation: 
        dp(i) = 1 + (dp(i-1) if nums[i]-nums[i-1] > 0 else 0)
        """
        maxSeen, curMax = 1, 1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]>0:
                print(i, nums[i]) 
                curMax += 1
            else:
                curMax = 1
            maxSeen = max(maxSeen, curMax)
        return maxSeen
