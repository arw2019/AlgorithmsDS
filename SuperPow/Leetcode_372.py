# solution using python's in-built pow function

class Solution:
    
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)

# an efficient recursive solution (AC)

class Solution:
    
    def __init__(self):
        self.mod = 1337
    
    def helper(self, a: int, k: int) -> int:
        a %= self.mod
        res = 1
        for _ in range(k):
            res = (res * a) % self.mod
        return res
    
    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1
        last_digit = b.pop()
        return self.helper(self.superPow(a, b), 10) * self.helper(a, last_digit) % self.mod

# brute force solution (TLE)

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        res = 1
        for i, digit in enumerate(b[::-1]):
            y = (a**(10**i)) % mod
            res = (res * y**digit) % mod
        return res
