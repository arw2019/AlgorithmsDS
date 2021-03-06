# yet another implementation
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        bad, N = None, len(nums)
        for i in range(N-1):
            if nums[i]>nums[i+1]:
                if bad is not None: return False
                bad = i
        return (not bad) or (nums[bad-1]<=nums[bad+1]) or \
                (bad == N-2) or (nums[bad] <= nums[bad+2])
    

# alternative implementation of the same idea
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt, pprev, prev = 0, float('-inf'), nums[0]
        for num in nums[1:]:
            cur = num
            if prev > cur:
                cnt +=1
                if cnt==2: 
                    return False
                if pprev > cur: 
                    cur = prev
            pprev, prev = prev, cur
        return True

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        i = 1
        while i<len(nums) and cnt <= 1:
            if nums[i-1]>nums[i]:
                cnt+=1
                if i<2 or (nums[i-2] <= nums[i]):
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            i+=1 
        return cnt <= 1
