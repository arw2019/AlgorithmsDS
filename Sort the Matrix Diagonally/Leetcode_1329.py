from collections import defaultdict

class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if not (matrix and matrix[0]): return [[]]
        m, n = len(matrix), len(matrix[0])
        
        diagonals = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                diagonals[j-i] += [matrix[i][j]]
        
        for _, vals in diagonals.items():
            vals.sort(reverse=True)
            
        for i in range(m):
            for j in range(n):
                matrix[i][j] = diagonals[j-i].pop()
                
        return matrix
