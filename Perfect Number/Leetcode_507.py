# sample idea but more efficient
# avoid division by large numbers
import math 

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num < 2: return False
        
        _sum = 1
        
        for x in range(2, 
                       math.ceil(math.sqrt(num))
                      ):
            if num % x == 0: 
                _sum += x
                _sum += num//x
                
        return _sum == num

# brute force - TLE

from math import sqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        divisors = []
        
        for x in range(1,int(num//2+1)):
            if num % x == 0: divisors.append(x)
                
        return sum(divisors) == num
