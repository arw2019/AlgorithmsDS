# 356ms - top 0.2%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums += [0]
        k, ans = 0, 0
        for num in nums:
            if num: k += 1
            else:
                if ans < k:
                    ans = k
                k = 0
        return ans
 
# 408 ms top 30%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, end, ans = 0, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                start, end = i+1, i+1
            else:
                end += 1
            ans = max(ans, end-start)
        return ans