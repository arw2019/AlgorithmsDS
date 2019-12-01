class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        pts = [(r, c) for r in range(R) for c in range(C)]
        return sorted(pts, key = lambda x: abs(x[0]-r0) + abs(x[1]-c0))
                