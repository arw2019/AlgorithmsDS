# top 5%
# use bit operator to compute parity of each element in array
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = [0]*n, [0]*m
        for ri, ci in indices:
            rows[ri] ^= 1
            cols[ci] ^= 1
        return sum(r^c for r in rows for c in cols)

# very slow, brute force solution
# class Solution:
#     def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
#         arr = [ [0 for _ in range(m)] for _ in range(n)]
#         for ri, ci in indices:
#             for i in range(n):
#                 arr[i][ci] += 1
#             for j in range(m):
#                 arr[ri][j] += 1
        
#         ans = 0
                
#         for i in range(n):
#             for j in range(m):
#                 if arr[i][j] % 2:
#                     ans +=1
        
#         return ans
