from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        return sum(max(0, freq-ct[char]) for char, freq in cs.items()) 
