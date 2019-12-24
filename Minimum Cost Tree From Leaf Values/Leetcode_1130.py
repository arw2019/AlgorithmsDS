class Solution:
    def mctFromLeafValues(self, vals: List[int]) -> int:
        ans, N = 0, len(vals)
        stack = [float('inf')]
        for v in vals:
            while stack[-1] <= v:
                v2 = stack.pop()
                ans += v2 * min(stack[-1], v)
            stack += [v]
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans
