from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        self.critical_connections = []
        
        self.graph = defaultdict(list)
        for u, v in connections:
            self.graph[u] += [v]
            self.graph[v] += [u]
            
        self.discovery_time = defaultdict(lambda: float('inf'))
        self.earliest_reachable = defaultdict(lambda: float('inf'))
        self.parent = defaultdict(lambda: -1)
        
        self.seen, self.Time = set(), 0
        
        
        def dfs(u: int) -> None:
            self.seen.add(u)
            self.discovery_time[u] = self.Time
            self.earliest_reachable[u] = self.Time
            self.Time += 1
            
            for v in self.graph[u]:
                if v not in self.seen:
                    self.parent[v] = u
                    dfs(v)
                    
                    self.earliest_reachable[u] = min(self.earliest_reachable[u], self.earliest_reachable[v])
                    
                    if self.earliest_reachable[v] > self.discovery_time[u]:
                        self.critical_connections += [[u, v]]
                elif v!= self.parent[u]:
                    self.earliest_reachable[u] = min(self.earliest_reachable[u], self.discovery_time[v])
        
        for u in range(n):
            if u not in self.seen:
                dfs(u)
        
        return self.critical_connections