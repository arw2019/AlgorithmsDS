class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        try:
            m, n = len(A), len(A[0])
        except IndexError:
            return 0
        
        return sum(
            any(
                A[i-1][j] > A[i][j] 
                for i in range(1, m)
            ) 
            for j in range(n)
        )
