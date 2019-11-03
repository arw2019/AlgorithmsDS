class Solution:
    
    def __init__(self):
        self.s = ''
        self.cache = {}
    
    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        return self.helper(0, len(s)-1)
        
    def helper(self, i, j) -> int:
        if (i,j) in self.cache: return self.cache[(i, j)]
        if i==j: 
            self.cache[(i, j)] = 1
        elif self.s[i] == self.s[j]:
            if i+1==j: 
                self.cache[(i, j)] = 2
            else:
                self.cache[(i, j)] = 2 + self.helper(i+1, j-1)
        else:
            self.cache[(i, j)] = max(self.helper(i+1, j), self.helper(i, j-1))
        return self.cache[(i,j)]
