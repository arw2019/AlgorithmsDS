from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        projs = sorted(zip(Profits, Capital), key=lambda x: x[1])
        pq = []
        totCap, j = W, 0
        for _ in range(k):
            while j < len(projs)  and projs[j][1] <= totCap:
                heappush(pq, -projs[j][0])
                j += 1 
            if pq: totCap -= heappop(pq)
        return totCap
