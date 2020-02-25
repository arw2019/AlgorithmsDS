from collections import deque

class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        
        seen = {}
        for u in range(len(adj)):
            if u not in seen and not self.check(adj, u, seen):
                return False
        
        return True
    
    def check(self, adj, u, seen):
        q = deque([(u, 1)])
        while q:
            pop, color = q.popleft()
            if pop in seen:
                if color != seen[pop]:
                    return False
            else:    
                seen[pop] = color
                for v in adj[pop]:
                    q.append((v, -color))
        return True
