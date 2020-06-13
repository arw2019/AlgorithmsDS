class Solution:
    def arrangeCoins(self, n: int) -> int:
        res, i = 0, 1
        while n:
            if n >= i:
                res += 1
                n -= i
                i += 1
            else:
                break
        return res
