class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.debug = False
        
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
            self.mat = [[0 for _ in range(n)] for _ in range(m)]       
            for row in range(m):
                for col in range(n):
                    self.mat[row][col] = self.mat[row][col-1] + matrix[row][col] \
                        if col > 0 else matrix[row][col]
                    if self.debug: print(f'self.mat[{row}][{col}] = {self.mat[row][col]}')
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = 0
        
        if self.debug: print(f'Query: row1={row1}, col1={col1}, row2={row2}, col2={col2}')
        
        for row in range(row1, row2+1):
            upper = self.mat[row][col2]
            lower = self.mat[row][col1-1] if col1 > 0 else 0
            _sum += upper - lower
            if self.debug: print(f'row={row}: _sum += {upper} - {lower}')
            
            
        return _sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
