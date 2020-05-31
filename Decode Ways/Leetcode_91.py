from functools import lru_cache
class Solution:
    @lru_cache()
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0": return 0
        if len(s)==1: return 1
        if int(s[0:2]) > 26:
            ans = self.numDecodings(s[1:])
            return ans
        else:
            ans = self.numDecodings(s[1:]) + (self.numDecodings(s[2:]) if len(s)>2 else 1)
            return ans
        
