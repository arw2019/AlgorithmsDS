from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        if not nums: return True
        
        queue  = defaultdict(list) # key = value of last element in subsequence; value = [(length_of_subsequence, subsequence_identifier)]
        
        for num in nums:
            if queue[num-1]:
                length = heappop(queue[num-1])
                heappush(queue[num], length+1)
            else:
                heappush(queue[num], 1)
        
        for heap in queue.values():
            while heap:
                if heap.pop() < 3: return False
        
        return True