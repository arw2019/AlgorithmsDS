class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        manhattan_distance = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        maxDist = float('-inf')
        res = 0
        for nutId, nutLoc in enumerate(nuts):
            d = manhattan_distance(nuts[nutId], tree)
            res += 2*d
            maxDist = max(maxDist, d - manhattan_distance(squirrel, nutLoc))
        return res - maxDist
    
