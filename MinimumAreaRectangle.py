"""
Leetcode 939

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = sorted(points)

        pts = set()
        for i in range(len(points)):
            pts.add((points[i][0], points[i][1]))
        
        res = float('inf')
        
        from collections import defaultdict
        dx, dy = defaultdict(list), defaultdict(list)
        
        for i in range(len(points)):
            dx[points[i][0]].append(i)
            dy[points[i][1]].append(i)
                        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in dx[x1]:
                if j!=i and j>i:
                    y2 = points[j][1]
                    for k in dy[y1]:
                        if k!=i and k>i: 
                            x2 = points[k][0]
                            if (x2, y2) in pts:
                                #print(x1, y1, x2, y2)
                                res = min(res, abs((x2-x1)*(y2-y1)))
                                
        if res == float('inf'): return 0                        
        return res