# 20x faster - uses binary search
from bisect import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
            
        w = sorted(word.count(min(word)) for word in words)
 
        return [len(w) - bisect(w, q.count(min(q))) for q in queries]
        
        
# correct but slower
from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s: str) -> List:
            c = Counter(s)
            smallest_char = sorted(c.keys())[0]
            return smallest_char, c[smallest_char]
        
        funcValsQ, funcValsW =[f(query) for query in queries], [f(word) for word in words]
        
        return [sum(funcValQ[1] < funcValW[1] for funcValW in funcValsW) for funcValQ in funcValsQ]
