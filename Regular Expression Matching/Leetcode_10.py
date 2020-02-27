# a more readable version of the same algorithm

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1) ]
        
        dp[0][0] = True
        for j in range(2, len(p)+1):
            dp[0][j] = (p[j-1]=='*') and dp[0][j-2]
        
        
        for j in range(1, len(p)+1):
            for i in range(1, len(s)+1):
                if p[j-1] in (s[i-1], '.'):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (p[j-2] in ('.', s[i-1]) and dp[i-1][j])
        
        return dp[len(s)][len(p)]

# dynamic program
# O(nm) runtime
class Solution:
    def isMatch(self, s: 'input, str', p: 'pattern, str') -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1]=True
        for i in range(m):
            for j in range(n):
                if p[j] in ('.', s[i]):
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1]!='.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:  
                        dp[i+1][j+1] = dp[i+1][j] or \
                                dp[i][j+1] or dp[i+1][j-1]
        return dp[-1][-1]

# great explanation: https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
