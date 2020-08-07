class Solution {
    public boolean isMatch(String s, String p) {
        int m = p.length(), n=s.length();
        boolean[][] dp = new boolean[n+1][m+1];
        
        for (int i=0; i<n+1; i++){
            for (int j=0; j<m+1; j++){
                if (i == 0){
                    if (j == 0) dp[i][j] = true;
                    else dp[i][j] = p.charAt(j-1) == '*' && dp[i][j-2];
                } else if (j==0) continue;
                else if (p.charAt(j-1) == s.charAt(i-1) || p.charAt(j-1) == '.'){
                    dp[i][j] = dp[i-1][j-1];
                } else if (p.charAt(j-1) == '*'){
                    dp[i][j] = dp[i][j-2];
                    if (!dp[i][j] && (p.charAt(j-2) == s.charAt(i-1) || p.charAt(j-2) == '.')){
                        dp[i][j] = dp[i-1][j] || dp[i][j-1];
                    }
                }
                else dp[i][j] = false;
            }
        }
        return dp[n][m];
    }
}
