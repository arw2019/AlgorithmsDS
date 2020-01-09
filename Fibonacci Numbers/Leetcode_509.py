class Solution:
    
    from functools import lru_cache

    @lru_cache()
    def fib(self, N: int) -> int:
        if N == 0: return 0
        elif N <= 2: return 1
        else:
            return self.fib(N-1) + self.fib(N-2)
