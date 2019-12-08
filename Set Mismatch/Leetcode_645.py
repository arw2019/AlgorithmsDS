# a more concise version
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, S = len(nums), sum({*nums})
        return sum(nums) - S, n*(n+1)//2 - S
    
# class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen, dup = set(), None
        i, n = 0, len(nums)
        while i < n:
            if nums[i] not in seen: seen.add(nums[i])
            else: 
                dup = nums[i]
                break
            i += 1
        return [dup, n*(n+1)//2 + dup - sum(nums)]
