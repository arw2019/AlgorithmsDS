class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0]*(N+1)
        maxVal = {} 
        for i in range(N+1):
            for j in range(1, K+1):
                if j<=i:
                    if (i,j) not in maxVal: 
                        maxVal[i,j] = max((A[m] for m in range(i-j, i)))
                    newVal = dp[i-j] + j * maxVal[i,j]
                    # print(newVal)
                    if newVal > dp[i]: dp[i] = newVal
            # print(dp)
        return dp[-1]
