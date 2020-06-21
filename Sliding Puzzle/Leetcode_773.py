from copy import deepcopy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = str([[1,2,3],[4,5,0]])
        if str(board) == target: return 0
        seen = set()
        curLevel = [board]
        numMoves = 0
        while curLevel:
            nextLevel = []
            numMoves += 1
            for cur in curLevel:
                seen.add(str(cur))
                i, j = next((i,j) for i in range(2) for j in range(3) if cur[i][j]==0)
                # swap vertically
                vert = deepcopy(cur)
                vert[i][j], vert[i-1][j] = vert[i-1][j], vert[i][j]
                if str(vert) not in seen: 
                    nextLevel += [vert]
                    seen.add(str(vert))
                # swap left
                if j>0:
                    left = deepcopy(cur)
                    left[i][j], left[i][j-1] = left[i][j-1], left[i][j]
                    if str(left) not in seen: 
                        nextLevel += [left]     
                        seen.add(str(left))
                # swap right
                if j<2:
                    right = deepcopy(cur)
                    right[i][j], right[i][j+1] = right[i][j+1], right[i][j]
                    if str(right) not in seen:
                        nextLevel += [right]
                        seen.add(str(right))
                if target in seen:
                    return numMoves
            curLevel.clear()
            curLevel += nextLevel
        return -1
