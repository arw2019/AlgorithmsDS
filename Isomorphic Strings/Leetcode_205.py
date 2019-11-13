# top 0.1%
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = {}
        reverse_hmap = {}
        
        for i, j in zip(s, t):
            if i not in hmap: 
                hmap[i] = j
        
        return t == ''.join([hmap[c] for c in s]) and len(set(hmap.values())) == len(hmap)
        
# top 40%
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t): return False
        
        ds, dt = defaultdict(list), defaultdict(list)
        [ds[char].append(i) for i, char in enumerate(s)]
        [dt[char].append(i) for i, char in enumerate(t)]
        
        S, T = set(), set()
        [S.add(str(v)) for k, v in ds.items()]
        [T.add(str(v)) for k, v in dt.items()]
        
        return S == T
