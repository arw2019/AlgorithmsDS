# top 8%

from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.rows = [defaultdict(int) for _ in range(9)]
        self.cols = [defaultdict(int) for _ in range(9)]
        self.subboxes = [[defaultdict(int) for _ in range(3)] for _ in range(3)]
    
    def validate(self, board: List[List[int]], i: int, j: int) -> set:
        ans = set()
        for num in range(1, 10):
            x = str(num)
            if self.rows[i][x] == 0 and self.cols[j][x] == 0 and self.subboxes[i//3][j//3][x] == 0:
                ans.add(x)
        return ans
    
    def dfs(self, board: List[List[int]], d: int) -> bool:
        if d == 81: return True # found solution
        i, j = d //9, d % 9
        if board[i][j] != '.': return self.dfs(board,d+1)
        possibilities = self.validate(board, i, j)
        for x in possibilities:
            board[i][j] = x
            self.rows[i][x] += 1
            self.cols[j][x] += 1
            self.subboxes[i//3][j//3][x] += 1
            if self.dfs(board, d+1):
                return True
            board[i][j] = '.'
            self.rows[i][x] -= 1
            self.cols[j][x] -= 1
            self.subboxes[i//3][j//3][x] -= 1
        return False
            
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = board[i][j]
                    self.rows[i][x] += 1
                    self.cols[j][x] += 1
                    self.subboxes[i//3][j//3][x] += 1
        self.dfs(board, 0)
