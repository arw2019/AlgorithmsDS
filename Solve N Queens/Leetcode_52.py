class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.result: int = 0
        self.col_placement = [0] * n
        
        def dfs(row: int) -> None:
            if row == n:
                # all the queens are legally placed
                self.result += 1
                return
            for col in range(n):
                if all (
                        abs(c-col) not in (0, row-i)
                        for i, c in enumerate(self.col_placement[:row])
                ):
                    self.col_placement[row] = col
                    dfs(row+1)
        
        dfs(0)
        
        return self.result