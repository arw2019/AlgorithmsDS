# top 2.5%
# O(N + mlgm) time where N=input_size and m=len(set(input))
# O(m) space 
import bisect
from collections import Counter

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = Counter(A)
        nums = sorted(c.keys(), key = lambda x: abs(x))
        seen = set()
        for n in nums:
            if n in seen or c[n] == 0: continue
            c[n*2] -= c[n]
            if c[n*2] < 0: return False
            seen.add(n)
        return True
        
        
# solution correct bad time complexity
# asymptotic complexity O(nlgn) - dominated by sorting array
# particularly slow for inputs with large numbers of repeats due to while loop
# import bisect
# class Solution:
#     def canReorderDoubled(self, A: List[int]) -> bool:
#         A.sort()
#         seen = set()
#         B = [(i, x) for i,x in enumerate(A)]
#         for i, a in sorted(B, key = lambda x: abs(x[1])):
#             if i in seen: continue
#             j = bisect.bisect_left(A, 2*a)
#             while j < len(A) and A[j] == 2*a and j in seen:
#                 j+=1
#             if j >= len(A) or A[j] != 2*a: return False
#             seen &= set([i,j])
#         return True
