class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        if self.m:
            self.n = len(matrix[0])
            if self.n:
                self.tree = [[0]*(self.n+1) for _ in range(self.m+1)]
                self.nums = [[0]*(self.n) for _ in range(self.m)]
                for i in range(self.m):
                    for j in range(self.n):
                        self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        if not (self.m or self.n): return
        delta = val - self.nums[row][col] 
        self.nums[row][col] = val
        i = row+1
        while i < self.m+1:
            j = col+1
            while j < self.n+1:
                self.tree[i][j] += delta
                j += j&(-j)
            i += i&(-i)
    
    def _sum(self, row: int, col: int) -> int:
        tot = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                tot += self.tree[i][j]        
                j -= j &(-j)
            i -= i&(-i)
        return tot

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not (self.m and self.n):
            return 0
        return self._sum(row2+1, col2+1) - self._sum(row1, col2+1) \
            - self._sum(row2+1, col1) + self._sum(row1, col1)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)