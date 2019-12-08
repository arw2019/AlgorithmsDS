import bisect
class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        h, H, m, M = list(map(int, [c for c in time if c.isdigit()]))
        A = sorted(list(set([h, H, m, M])))
        if len(A) == 1: return time
        
        if M != A[-1]: # increment first minutes digit
            return time[:-1] + str(A[A.index(M)+1])
        if A.index(m)+1 < len(A) and A[A.index(m)+1] < 6:  
            # increment second minutes digit
            return time[:3] + str(A[A.index(m)+1]) + str(A[0])
        
        if h == 2:
            if H == 3 or (A.index(H) < len(A) and A[A.index(H)+1] > 3):
                # roll over to the next day
                return str(A[0])*2 + ':' + str(A[0])*2
            # increment first hours digit
            return str(h) + str(A[A.index(H)+1]) + ':' + str(A[0])*2
        if A.index(H) + 1 < len(A):
            # increment first hours digit
            return str(h) + str(A[A.index(H)+1]) + ':' + str(A[0])*2
        if A[A.index(h)+1] * 10 + A[0] < 23:
            # increment second hours digit
            return str(A[A.index(h)+1]) + str(A[0]) + ':' + str(A[0])*2
        # roll over to the next day
        return str(A[0])*2 + ':' + str(A[0])*2
        
            
