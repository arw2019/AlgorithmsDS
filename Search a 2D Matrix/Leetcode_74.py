class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix and matrix[0]): return False
        firstCol = [row[0] for row in matrix] 
        i = bisect.bisect_right(firstCol, target)-1
        if i < 0: return False
        print(f"i={i}, {matrix[i]}")
        j = bisect.bisect_right(matrix[i], target) -1
        if j < 0: return False
        print(f"j={j}, {matrix[i][j]}")
        return matrix[i][j] == target
