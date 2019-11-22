from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # build the max-heap
        # -ve sign because heapq implements a min-heap
        heap = []
        for stone in stones: 
            heappush(heap, -stone)
            
        while len(heap) >= 2:
            x, y = heappop(heap), heappop(heap)
            if x != y:
                heappush(heap, -abs(y-x))
                
        return -heappop(heap) if heap else 0