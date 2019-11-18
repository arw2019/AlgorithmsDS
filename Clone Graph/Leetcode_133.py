"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.d = defaultdict(lambda: Node(None, []))
        self.d[None] = None
        
        def dfs(u: 'Node', seen: set = set()):
            seen.add(u)
            self.d[u].val = u.val
            for v in u.neighbors:
                self.d[u].neighbors += [self.d[v]]
                if v not in seen:
                    dfs(v, seen)
        
        dfs(node)
        return self.d[node]