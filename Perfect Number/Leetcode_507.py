# brute force - TLE

from math import sqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        divisors = []
        
        for x in range(1,int(num//2+1)):
            if num % x == 0: divisors.append(x)
                
        return sum(divisors) == num
