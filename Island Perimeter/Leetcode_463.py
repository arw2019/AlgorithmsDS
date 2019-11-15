# top 5%
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not (grid and grid[0]): return 0
        m, n = len(grid), len(grid[0])
        return sum([sum([j == 0 or grid[i][j-1] == 0, j == n-1 or grid[i][j+1] == 0,
                i == m-1 or grid[i+1][j] == 0, i == 0 or grid[i-1][j] == 0]) 
                    for i in range(m) for j in range(n) if grid[i][j] == 1])

# top 70%
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         if not (grid and grid[0]): return 0
#         m, n = len(grid), len(grid[0])
#         perimeter = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     north, south = (i == m-1), (i == 0)
#                     east, west = (j == 0), (j == n-1)
#                     if east or grid[i][j-1] == 0:
#                         perimeter += 1
#                     if west or grid[i][j+1] == 0:
#                         perimeter += 1
#                     if north or grid[i+1][j] == 0: 
#                         perimeter +=1
#                     if south or grid[i-1][j] == 0:
#                         perimeter +=1
#         return perimeter
