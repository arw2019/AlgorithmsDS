class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        lo, hi, t = 0, len(nums)-1, (target<nums[0], target)
        # this line is needed if nums contains duplicates
        while hi > 0 and nums[hi] == nums[lo]:
            hi-=1
        while lo <= hi:
            mid = (lo+hi)//2
            guess = (nums[mid] < nums[0], nums[mid])
            if guess == t: return True
            elif guess < t: lo=mid+1
            else: hi=mid-1
        return False
