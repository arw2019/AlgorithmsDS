from collections import defaultdict

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        debug = False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u] += [v]
            graph[v] += [u]
    
        termini = [u for u, neighbors in graph.items() \
                            if len(neighbors) == 1]
        
        self.res = 0
       
        def dfs(u, seen, parent,  dist):
            if u not in seen:
                if debug: 
                    print(f'node={u}, len={len(graph[u])}, seen={seen}, dist={dist}') 
                seen.add(u)
                if len(graph[u]) == 1:
                    if debug: 
                        print(f'current val: {self.res}, new val = {dist}')
                    self.res = max(self.res, dist)
            for v in graph[u]:
                if v not in seen:
                    dfs(v, seen, parent, dist+1)
    
        seen = set()
        for node in termini:
            dfs(node, seen, node, 0)
            seen.clear()
            
        return self.res
