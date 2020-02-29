class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, m, B, n = B, n, A, m
        if n == 0: raise ValueError
            
        idxMin, idxMax, halfLen = 0, m, (m+n+1)//2
        
        while True: 
            
            i = (idxMin + idxMax)//2
            j = halfLen - i
            
            if i < m and B[j-1] > A[i]:
                idxMin = i+1
            elif i > 0 and A[i-1] > B[j]:
                idxMax = i-1
            else:
                maxOfLeft = B[j-1] if i==0 else A[i-1] if j==0 else max(A[i-1],B[j-1])
                if (m+n)%2 == 1: 
                    return maxOfLeft
                minOfRight = B[j] if i==m else A[i] if j==n else min(A[i],B[j])
                return (maxOfLeft + minOfRight)/2.0
