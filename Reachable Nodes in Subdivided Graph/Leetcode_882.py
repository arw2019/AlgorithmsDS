from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        
        graph = defaultdict(dict)
        for u, v, n in edges:
            graph[u][v] = graph[v][u] = n
        
        heap, seen = [(-M, 0)], {}
                    
        while heap:
            no_moves, u = heappop(heap)
            if u not in seen:
                seen[u] = - no_moves
                for v in graph[u]:
                    no_moves2 = - no_moves - graph[u][v] - 1
                    if v not in seen and no_moves2 >= 0:
                        heappush(heap, (-no_moves2, v))
        ans = len(seen)
        for u, v, n in edges:
            ans += min(seen.get(u, 0) + seen.get(v, 0), graph[u][v])
        
        return ans