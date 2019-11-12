# top 0.5%
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # clockwise rotation = up-down flip followed by transposition
        matrix[:] = map(list, zip(*matrix[::-1]))
