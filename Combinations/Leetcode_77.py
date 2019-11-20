class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[_] for _ in range(1, n+1)]
        if k == n:
            return [[_ for _ in range(1, n+1)]]
        result = []
        result += self.combine(n-1, k)
        fragment = self.combine(n-1, k-1)
        for piece in fragment:
            piece += [n]
        result += fragment
        return result