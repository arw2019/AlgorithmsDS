# bottom-up DP
# O(n) time, O(1) space

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        num1, num2 = 1, 2
        for _ in range(n-2):
            num1, num2 = num2, num1+num2
        return num2
    
# top-down DP
# O(n) time, O(n) space

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
