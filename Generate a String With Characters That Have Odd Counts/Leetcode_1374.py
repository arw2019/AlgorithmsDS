class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1: 
            return 'p'
        elif n % 2 == 1:
            return 'p'*(n-2) + 'st' 
        else: # n%2 == 0
            return 'p'*(n-1) + 's'
