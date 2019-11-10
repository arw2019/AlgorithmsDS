#top 0.5%
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack, ans = [], 0
        i = 0
        while i < len(h):
            if (not stack) or (h[stack[-1]] <= h[i]):
                stack.append(i)
                i+=1
            else:
                j = stack.pop()
                area = h[j] * (i - stack[-1] - 1 if stack else i)
                ans = max(ans, area)
        while stack:
            j = stack.pop()
            area = h[j] * (i - stack[-1] - 1 if stack else i)
            ans = max(ans, area)
        return ans