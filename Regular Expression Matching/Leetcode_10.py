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
