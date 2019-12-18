class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n, inf = len(A), float('inf')
        def check(num: int):
            a, b  = 0, 0 
            for i in range(n):
                if not (A[i] == num or B[i] == num): return inf
                if A[i] != num: a += 1
                if B[i] != num: b += 1
            return min(a, b)
        ans = min(check(A[0]), check(B[0]))
        return ans if ans < inf else -1
