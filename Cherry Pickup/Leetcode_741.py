class Solution:
    def __init__(self):
        self.f = {}
    def cherryPickup(self, grid: List[List[int]]) -> int:
        return max(0, self.dfs(grid, len(grid), 0, 0, 0, 0))
    def dfs(self, g: List[List[int]], n: int, r1: int, c1: int, r2: int, c2: int) -> int:
        if (r1, c1, r2, c2) in self.f:
            pass
        elif max(r1, c1, r2, c2) >= n or g[r1][c1] == -1 or g[r2][c2] == -1:
            self.f[r1, c1, r2, c2] = float('-inf')
        elif r1 == c1 == n-1:
            return g[r1][c1]
        else:
            cherries = g[r1][c1] if (r1,c1)==(r2,c2) else g[r1][c1] + g[r2][c2]
            cherries += max(
                self.dfs(g, n, r1+1, c1, r2+1, c2),
                self.dfs(g, n, r1+1, c1, r2, c2+1),
                self.dfs(g, n, r1, c1+1, r2+1, c2),
                self.dfs(g, n, r1, c1+1, r2, c2+1)
            )
            self.f[r1,c1,r2,c2] = cherries
        return self.f[r1,c1,r2,c2]
