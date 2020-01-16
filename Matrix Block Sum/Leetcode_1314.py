# numpy solution - no caching
# AC, top 80%

import numpy as np

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        if not (mat and mat[0]): return [[]]
        
        mat_np = np.array(mat)
        m, n = len(mat), len(mat[0])
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                lowerRow, upperRow = max(0, i-K), min(m, i+K)
                lowerCol, upperCol = max(0, j-K), min(n, j+K)
                # print(f'row={i}, col={j}, row_limits=[{lowerRow},{upperRow}], col_limits=[{lowerCol},{upperCol}]')
                ans[i][j] = np.sum(mat_np[lowerRow:upperRow+1, lowerCol:upperCol+1])
        
        return ans
