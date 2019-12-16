class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        print(n%10)
        while n:
            digit, n = n%10, n // 10
            p *= digit
            s += digit
        return p - s
