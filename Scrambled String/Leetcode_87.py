# top 30%
# DP with memoization + subproblem pruning  
from collections import Counter
class Solution:
    def __init__(self):
        self._memo={}
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self._memo:
            return self._memo[(s1,s2)]
        if len(s1) != len(s2): # pruning
            self._memo[(s1,s2)] = False
        elif s1 == s2: # pruning
            self._memo[(s1,s2)] = True
        elif Counter(s1) != Counter(s2): # pruning
            self._memo[(s1,s2)] = False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:],s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:],s2[:-i])):
                self._memo[(s1,s2)] = True
                break
                
        if (s1, s2) not in self._memo: 
            self._memo[(s1,s2)] = False
            
        return self._memo[(s1,s2)]