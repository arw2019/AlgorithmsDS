 # brute force solution O(N^2)  
 
from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = defaultdict(list)
        for i, row in enumerate(mat):
            num_soldiers = sum(row)
            d[num_soldiers] += [i]
        weakest_rows = []
        for _, vals in sorted(d.items()):
            vals = vals[::-1]
            while len(weakest_rows) < k and vals:
                weakest_rows += [vals.pop()]
            if len(weakest_rows) == k:
                break
        return weakest_rows
