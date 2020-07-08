# my implementation of Tarjan's algorithm
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

# a cleaner implementation of the same algorithm
# from AC solutions on Leetcode
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [list() for _ in range(n)]
        visits = [-1]*n
        clock = 0
        critical_connections= list()
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node: int, parent: int) -> int:
            nonlocal clock
            nonlocal critical_connections
            clock += 1
            visits[node] = clock
            min_node = clock
            for neighbor in graph[node]:
                if visits[neighbor] == -1:
                    min_neighbor = dfs(neighbor, node)
                    min_node = min(min_node, min_neighbor)
                    if visits[node] < min_neighbor:
                        critical_connections.append((node, neighbor))
                elif neighbor != parent:
                    min_node = min(min_node, visits[neighbor])
            return min_node
       
        dfs(0, -1)
        
        return critical_connections
