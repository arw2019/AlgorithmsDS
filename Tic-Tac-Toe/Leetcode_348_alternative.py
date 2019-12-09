class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rowSum = [0]*n
        self.colSum = [0]*n
        self.diagSum = 0
        self.antiDiagSum = 0

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
        val = -1 if player == 1 else 1
        self.rowSum[row]+=val
        self.colSum[col]+=val
        if row == col: self.diagSum += val
        if row == self.n - 1 - col: self.antiDiagSum += val
        return self._isWinner(row, col, player)
    
    def _isWinner(self, row: int, col: int, player: int) -> bool:
        won = -self.n if player == 1 else self.n
        return player if (self.rowSum[row] == won or self.colSum[col] == won \
            or self.diagSum == won or self.antiDiagSum == won) else 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
