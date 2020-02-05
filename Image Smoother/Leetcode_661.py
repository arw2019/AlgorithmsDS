import math
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not (M and M[0]): return [[]] 
        m, n = len(M), len(M[0])
        res = [[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, cnt = M[i][j], 1
                if i > 0:
                    tot, cnt  = tot + M[i-1][j], cnt + 1
                if i < m-1:
                    tot, cnt  = tot + M[i+1][j], cnt + 1
                if j > 0:
                    tot, cnt  = tot + M[i][j-1], cnt + 1
                if j < n-1:
                    tot, cnt  = tot + M[i][j+1], cnt + 1
                if i > 0 and j > 0:
                    tot, cnt  = tot + M[i-1][j-1], cnt + 1
                if i < m-1 and j > 0:
                    tot, cnt  = tot + M[i+1][j-1], cnt + 1
                if i < m-1 and j < n-1:
                    tot, cnt  = tot + M[i+1][j+1], cnt + 1
                if i > 0 and j < n-1:
                    tot, cnt  = tot + M[i-1][j+1], cnt + 1
                # print(f'({i}, {j}), tot={tot}, cnt={cnt}')       
                res[i][j] = math.floor(tot/cnt)
        return res
