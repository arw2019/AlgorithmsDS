# O(N) time
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = nums
        for i in range(1, N):
            res[i] += res[i-1]
        return res

# O(N^2) time (but one-liner)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
