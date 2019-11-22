from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        heap = []
        for i, val in enumerate(values):
            heappush(heap, (-val, labels[i], i))
        
        maxTot, size, num_with_label = 0, 0, defaultdict(int)
        
        while size < num_wanted and heap:
            x = heappop(heap)
            if num_with_label[x[1]] < use_limit:
                num_with_label[x[1]] += 1
                size += 1
                maxTot += (-x[0])
        
        return maxTot