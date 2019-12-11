class Solution:
    def countSegments(self, s: str) -> int:
        return sum(len(x)>0 for x in s.split(' '))
