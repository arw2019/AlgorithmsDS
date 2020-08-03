class Solution {
public:
    bool isMatch(string s, string p) {
        int m=p.length(), n=s.length();
        vector<vector<bool>> dp(n+1, vector<bool>(m+1, false));
        
        for (int i=0; i<n+1; ++i){
            for (int j=0; j<m+1; ++j){
                if (i==0){
                    if (j==0) dp[i][j] = true;
                    else dp[i][j] = (p[j-1] == '*') && dp[i][j-2];
                }
                else if (j == 0) continue;
                else if (p[j-1] == s[i-1] || p[j-1] == '.') dp[i][j] = dp[i-1][j-1];
                else if (p[j-1] == '*'){
                    dp[i][j] = dp[i][j-2];
                    if (!dp[i][j] && ((p[j-2] == s[i-1]) || (p[j-2] == '.'))){
                        dp[i][j] = dp[i-1][j] || dp[i][j-1];
                    } 
                }
            }
        }
        return dp[n][m];
    }
};
