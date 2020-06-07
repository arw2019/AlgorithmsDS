class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, seen=set()):
            if (i,j) not in seen and 0<=i<m and 0<=j<n and board[i][j] == word[len(seen)]:
                seen.add((i,j))
                if len(seen) == len(word): 
                    return True
                else:
                    res = dfs(i-1, j) or dfs(i+1, j) or dfs(i, j-1) or dfs(i, j+1)
                    if res: return True
                    else: seen.remove((i,j))
        return any(dfs(i,j) for j in range(n) for i in range(m))
