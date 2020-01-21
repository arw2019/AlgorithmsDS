class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res, power = 1.0, n
        
        if n < 0: 
            power, x = -power, 1.0/x
        
        while power:
            if power & 1:
                res *= x
            x, power = x*x, power >> 1
        
        return res
