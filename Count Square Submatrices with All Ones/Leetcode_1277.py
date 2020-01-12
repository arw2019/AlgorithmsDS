# much faster (~600ms) single pass solution

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i-1][j] \
                        and matrix[i][j-1] and matrix[i-1][j-1]:
                    matrix[i][j] = min(matrix[i-1][j], 
                                   matrix[i][j-1], 
                                   matrix[i-1][j-1]) + 1
        
        return sum(matrix[i][j] for i in range(m) for j in range(n))

# correct but relatively slow (~1200ms)

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        def check(i, j, h, cur, _next):
            if h == 1:
                if matrix[i][j]: 
                    _next.add((i, j))
            elif i>=m or j >=n or i+h-1>= m or j+h-1>= n:
                return False
            elif (i, j) in cur and  \
                        all(matrix[i+h-1][J] for J in range(j,j+h))  and \
                        all(matrix[I][j+h-1] for I in range(i, i+h)):
                _next.add((i, j))
               
        _next = set()
        cur = ((i,j) for i in range(m) for j in range(n))
        count, H = 0, 1
        
        
        while cur:
            for i, j in cur:
                check(i, j, H, cur, _next)
            count += len(_next)
            # print(f'there are {len(_next)} squares of side {H}')
            cur, _next = _next, set()
            H += 1
                              
        return count
