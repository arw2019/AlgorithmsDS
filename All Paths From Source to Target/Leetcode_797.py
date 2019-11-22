class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        N, res = len(graph), []
        
        queue = [[0]]
        while queue:
            newQueue = []
            for path in queue:
                for v in graph[path[-1]]:
                    if v == N-1: 
                        res += [path + [v]]
                    else:
                        newQueue += [path + [v]]
            queue = newQueue
        
        return res
