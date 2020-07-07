class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack, ans = [], 0
        N, i = len(h), 0
        while i < N or stack:
            if i<N and (not stack or h[stack[-1]] <= h[i]):
                stack.append(i)
                i+=1
            else:
                j = stack.pop()
                area = h[j] * (i - stack[-1] - 1 if stack else i)
                ans = max(ans, area)
        return ans
