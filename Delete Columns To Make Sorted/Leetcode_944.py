class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        cnt = 0
        for j in range(n):
            for i in range(1,m):
                if A[i-1][j] > A[i][j]:
                    cnt+=1
                    break
        return cnt
