# numpy solution with caching 
# AC, ~204ms
import numpy as np

class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], K: int) -> List[List[int]]:
        
        if not (matrix and matrix[0]): return [[]]
        
        m, n = len(matrix), len(matrix[0])
        mat = np.array(matrix)
        
        for i in range(1,m):
            for j in range(n):
                mat[i,j] += mat[i-1,j]
        for j in range(1,n):
            for i in range(m):
                mat[i,j] += mat[i,j-1]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                lowerRow, upperRow = max(0, i-K), min(m-1, i+K)
                lowerCol, upperCol = max(0, j-K), min(n-1, j+K)
                sum1 = mat[upperRow, upperCol]
                sum2 = mat[lowerRow-1, upperCol] if lowerRow>0 else 0
                sum3 = mat[upperRow,lowerCol-1] if lowerCol>0 else 0
                sum4 = mat[lowerRow-1, lowerCol-1] if (lowerRow>0 and lowerCol>0) else 0
                ans[i][j] = sum1-sum2-sum3+sum4
        
        return ans

# numpy solution - no caching
# AC, ~360ms

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
