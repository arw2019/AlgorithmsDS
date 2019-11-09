from collections import Counter
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = Counter(nums)
        for num in sorted(cnt.keys()):
            ans += [num]*cnt[num]
        return ans
