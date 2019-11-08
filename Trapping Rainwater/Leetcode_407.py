# top 4%
from heapq import heappush, heappop
class Solution:
    def trapRainWater(self, A: List[List[int]]) -> int:
        
        if not (A and A[0]): return 0
        
        m, n = len(A), len(A[0])
        
        heap = []
        # heap holds tuples (height, i, j)
        
        for i in range(m):
            for j in range(n):
                if A[i][j] > 0 and (i == 0 or i == m-1 or j == 0 or j == n-1):
                    heappush(heap, (A[i][j], i, j))
                    A[i][j] = 'X'
        
        ans = 0
        
        while heap:
            h, i, j = heappop(heap)
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0<=x<m and 0<=y<n and A[x][y] != 'X':
                    ans += max(0, h-A[x][y])
                    heappush(heap, (max(h, A[x][y]), x, y))
                    A[x][y] = 'X'
        return ans
