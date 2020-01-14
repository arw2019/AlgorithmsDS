#correct but TLE

from collections import namedtuple
from heapq import heappush, heappop

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        heap = [] # a min-heap with distance between workers and bikes as key
        
        Pair = namedtuple('Pair', 'distance worker_id bike_id')
        
        for worker_id, worker_location in enumerate(workers):
            for bike_id, bike_location in enumerate(bikes):
                heappush(heap, Pair(
                        manhattan(worker_location, bike_location),
                        worker_id,
                        bike_id
                ))
    
        ans = [-1] * len(workers)
        taken = set()
        while heap:
            pair = heappop(heap)
            if ans[pair.worker_id] == -1 and pair.bike_id not in taken:
                ans[pair.worker_id] = pair.bike_id
                taken.add(pair.bike_id)
        
        return ans
