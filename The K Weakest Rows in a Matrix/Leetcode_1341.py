# linear time solution 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not (mat and mat[0]) or k > len(mat): 
            return []
        m, n = len(mat), len(mat[0])
        weakest_rows = []
        col = 0
        seen = set()
        while col < n and len(weakest_rows) < k:
            zeros = [i for i, row in enumerate(mat) 
                     if row[col] == 0 and i not in seen]
            seen |= set(zeros)       
            weakest_rows += zeros
            col += 1
        i = 0
        while len(weakest_rows) < k:
                if i not in seen: weakest_rows.append(i)
                i+=1 
        return weakest_rows[:k]
   

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
