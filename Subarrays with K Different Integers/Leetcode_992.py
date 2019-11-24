from collections import defaultdict
class Solution:        
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        i, k, ans = 0, 0, 0
        d = defaultdict(int)
        for j in range(len(A)):
            d[A[j]] += 1
            if len(d) < K:
                continue
            elif len(d) > K:
                d.pop(A[k])
                k += 1
                i = k
            while d[A[k]] > 1:
                d[A[k]] -= 1
                k += 1
            ans += k - i + 1
        return ans
