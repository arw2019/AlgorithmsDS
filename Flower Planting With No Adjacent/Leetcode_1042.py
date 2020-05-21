class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in paths:
            g[u] += [v]
            g[v] += [u]
        colors = [None]*(N+1)
        for u in range(1, N+1):
            if colors[u]: continue
            available = {1,2,3,4} - {colors[v] for v in g[u] if colors[v]}
            colors[u] = available.pop()
        return colors[1:]
