#top 0.4%
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        n = int(math.sqrt(N))
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        subboxes = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
        for i in range(N):
            for j in range(N):
                num = board[i][j]
                if num != '.':
                    rows[i][num] += 1
                    cols[j][num] += 1
                    subboxes[i//n][j//n][num] +=1
                    if rows[i][num] > 1 or cols[j][num] > 1 or subboxes[i//n][j//n][num] > 1:
                        return False
        return True
    