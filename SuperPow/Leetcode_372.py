# brute force solution (TLE)

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        res = 1
        for i, digit in enumerate(b[::-1]):
            y = (a**(10**i)) % mod
            res = (res * y**digit) % mod
        return res
