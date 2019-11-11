# top 1%
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans, curMin, curMax = 0, 10000, -10000
        for a in arrays:
            ans = max(ans, max(a[-1]-curMin, curMax-a[0]))
            curMin, curMax = min(curMin, a[0]),  max(curMax, a[-1])
        return ans
