# O(NlgN) time

from heapq import heappop, heappush
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks) # O(N)
        cost=0
        while len(sticks)>1: # O(N) executions
            l, r = heappop(sticks), heappop(sticks) # O(N) time 
            cost += l + r
            heappush(sticks, l+r) # O(N) time
        return cost
