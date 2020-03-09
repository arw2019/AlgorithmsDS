from functools import lru_cache

class Solution:
    
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        if n>2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        elif n==2:
            return 2
        else:
            return 1
