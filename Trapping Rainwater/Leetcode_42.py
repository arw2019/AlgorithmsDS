# top 1%
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxLeft, maxRight = 0, 0
        ans = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else: # height[right] > height[left]
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans
