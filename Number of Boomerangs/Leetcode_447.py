from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        for i in range(N):
            d = defaultdict(int)
            for j in range(N):
                p, q = points[i], points[j]
                dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
                res += 2 * d[dist]
                d[dist] += 1
        return res
