# top 8%
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = {str(cells): N}
        while N>0:
            visited.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1,7)] + [0]
            if str(cells) in visited:
                N %= visited[str(cells)] - N
        return cells
        

# brute force, TLE
# class Solution:
#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         while N > 0:
#             N -= 1
#             dummy = [0]*8
#             for i in range(1,7):
#                 if cells[i-1] == cells[i+1]: dummy[i] = 1
#             cells = dummy
#         return cells
