class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        def diff(i: int) -> int:
            mod = 1440
            minutes = lambda x: int(x[:2])*60 + int(x[3:])
            m1, m2 = minutes(timePoints[i-1]), minutes(timePoints[i])
            return min((m1-m2) % mod, (m2-m1) % mod)
        
        return min(diff(i) for i in range(len(timePoints)))
