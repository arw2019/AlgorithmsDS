from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        deg, adj = defaultdict(int), defaultdict(list)
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            adj[u] += [v]
            adj[v] += [u]
        unseen = set(range(n))
        priorLevel = [v for v, degree in deg.items() if degree == 1]
        while len(unseen) > 2:
            currentLevel = []
            for u in priorLevel:
                unseen.remove(u)
                for v in adj[u]:
                    if v in unseen:
                        deg[v] -= 1
                        if deg[v] == 1: 
                            currentLevel += [v]
                priorLevel = currentLevel
        return priorLevel
