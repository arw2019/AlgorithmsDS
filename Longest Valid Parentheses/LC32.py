class Solution:    
    def longestValidParentheses(self, s: str) -> int:
        dp, stack = [0]*(len(s)+1), []
        for idx1, paren in enumerate(s):
            if paren == '(': stack += [idx1]
            elif stack:
                idx2 = stack.pop()
                dp[idx1+1] = dp[idx2] + idx1 - idx2 + 1
        return max(dp)
                
