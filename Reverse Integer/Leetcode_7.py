class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            res = res*10 + x % 10
            x = x //10
        return 0 if (res < -2147483648 or res > 2147483647) else sign * res
