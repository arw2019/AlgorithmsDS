class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
       
        max_seen, max_end = float('-inf') , 0
        min_seen, min_end = float('inf'), 0
        tot = 0
        for a in A:
            max_end = max(a, a + max_end)
            max_seen = max(max_seen, max_end)
            min_end = min(a, a + min_end)
            min_seen = min(min_seen, min_end)
            tot += a
        return max(max_seen, tot-min_seen) if max_seen > 0 else max_seen
