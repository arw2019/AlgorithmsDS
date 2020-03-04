class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        isPrime = [False]*2 + [True]*(n-1)
        for p in range(2, n):
            if isPrime[p]:
                res += 1
                for r in range(2*p, n+1, p):
                    isPrime[r] = False
        return res
