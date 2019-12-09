class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self._players =  {1: [[False]*n for _ in range(n)], 2: [[False]*n for _ in range(n)]}
    
    def _isWinning(self, player: int) -> bool:
        # check rows
        for i in range(self.n):
            if all(self._players[player][i]): return True
        # check columns
        for j in range(self.n):
            if all(self._players[player][i][j] for i in range(self.n)): return True
        # check diagonals
        for i in range(self.n):
            if all(self._players[player][i][i] for i in range(self.n)): return True
            if all(self._players[player][i][self.n-1-i] for i in range(self.n)): return True
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self._players[player][row][col] = True
        if self._isWinning(player): 
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
