class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.result: List[List[int]] = []
        self.col_placement = [0] * n
        
        def solve_n_queens(row: int) -> None:
            if row == n:
                # all the queens are legally placed
                self.result += [self.col_placement.copy()]
                return
            for col in range(n):
                if all (
                        abs(c-col) not in (0, row-i)
                        for i, c in enumerate(self.col_placement[:row])
                ):
                    self.col_placement[row] = col
                    solve_n_queens(row+1)
        
        solve_n_queens(0)
        
        return [ ['.' * i + 'Q' + '.'*(n-i-1) for i in solution] for solution in self.result]