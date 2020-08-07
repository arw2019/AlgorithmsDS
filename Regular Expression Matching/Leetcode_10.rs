impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let (m, n) = (p.len(), s.len());
        let S: Vec<char> =(&s).chars().collect();
        let P: Vec<char> = (&p).chars().collect();
        let mut dp = vec![vec![false; m+1]; n+1];
        for i in 0..n+1{
            for j in 0..m+1{
                if (i == 0){
                    if(j == 0) { dp[i][j] = true; }
                    else { dp[i][j] =(P[j-1] == '*') && dp[i][j-2]; }
                } 
                else if(j==0){ continue; }
                else if(P[j-1]=='.' || P[j-1]==S[i-1]){
                    dp[i][j] = dp[i-1][j-1];    
                } else if (P[j-1] == '*'){
                    dp[i][j] = dp[i][j-2];
                    if (!dp[i][j] && (P[j-2]=='.' || P[j-2]==S[i-1])){
                        dp[i][j] = dp[i-1][j] || dp[i][j-1];
                    }
                }
            }
        }
        return dp[n][m];
    }
}
