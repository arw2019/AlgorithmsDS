class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in paths:
            g[u-1] += [v-1]
            g[v-1] += [u-1]
        colors = [None]*N
        for u in range(N):
            if not colors[u]:
                available = {1,2,3,4} - {colors[v] for v in g[u] if colors[v]}
                colors[u] = available.pop()
        return colors
