    def countLetters(self, S: str) -> int:
        n = len(S)
        dp = [1] * n
        for i in range(n-2, -1, -1):
            if S[i]==S[i+1]: dp[i] = dp[i+1]+1
        return sum(dp)
