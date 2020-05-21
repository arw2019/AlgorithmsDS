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
        # print(g)
        for deg in (3, 2, 1):
            for u in degrees[deg]:
                if colors[u]: continue
                available = allColors - {colors[v] for v in g[u] if colors[v]}
                # for v in g[u]:
                #     print(v, colors[v])
                #     available.discard(colors[v])
                # print(f"colors={colors}, v={v}, avail={available}")
                colors[u] = available.pop()
                # print(f"u={u}, coloring={colors[u]}")
        return colors[1:]
