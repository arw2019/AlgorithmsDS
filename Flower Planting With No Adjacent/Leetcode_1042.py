import random
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        allColors = {1, 2, 3, 4}
        g = defaultdict(list)
        degrees = defaultdict(list)
        for u, v in paths:
            g[u] += [v]
            g[v] += [u]
        for u, neighbours in g.items():
            degrees[len(neighbours)] += [u]
        colors = [None]*(1+N)
        for deg in (3, 2, 1):
            for u in degrees[deg]:
                if colors[u]: continue
                available = allColors - {colors[v] for v in g[u] if colors[v]}
                colors[u] = available.pop()
        for i in range(1, N+1):
            if not colors[i]: colors[i]=1
        return colors[1:]
