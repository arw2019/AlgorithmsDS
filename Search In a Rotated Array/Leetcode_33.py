class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        lo, hi, t = 0, len(nums)-1, (target<nums[0], target)
        while lo <= hi:
            mid = (lo+hi)//2
            guess = (nums[mid] < nums[0], nums[mid])
            if guess == t: return mid
            elif guess < t: lo=mid+1
            else: hi=mid-1
        return -1
