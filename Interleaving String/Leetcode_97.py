# top 5%
class Solution:
    def __init__(self):
        self.cache = {('','',''): True}
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if (s1, s2, s3) in self.cache: 
            return self.cache[s1, s2, s3] 
        if s1 and  s1[0] == s3[0]:
            self.cache[s1[1:], s2, s3[1:]] = self.isInterleave(s1[1:], s2, s3[1:])
            if self.cache[s1[1:], s2, s3[1:]]: 
                return self.cache[s1[1:], s2, s3[1:]]
        if s2 and s2[0] == s3[0]:
            self.cache[s1, s2[1:], s3[1:]] = self.isInterleave(s1, s2[1:], s3[1:])
            return self.cache[s1, s2[1:], s3[1:]] 