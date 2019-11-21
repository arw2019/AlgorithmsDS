# top 0.8%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        slope = None
        
        for i in range(2, n):
            
            x1, y1 = coordinates[i-1]
            x2, y2 = coordinates[i]
            
            # print(x1, y1, x2, y2)
            
            if x1 == x2:
                if y1 == y2: continue
                else: return False
                
            if slope is None:
                slope = (y2 - y1)/(x1 - x2)
                
            if (y2 - y1)/(x1 - x2) != slope:
                return False
            
        return True
