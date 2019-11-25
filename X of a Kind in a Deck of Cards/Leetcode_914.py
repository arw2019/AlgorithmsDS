from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if not deck: return False
        
        c = Counter(deck)
        occurences = sorted(c.values())
        
        if len(occurences) == 1: return occurences[0] > 1
        
        smallest_poss = math.gcd(occurences[0], occurences[1])
        for j in range(2, len(occurences)):
            smallest_poss = math.gcd(smallest_poss, occurences[j])
        
        return all([occ % smallest_poss == 0 for occ in occurences]) if smallest_poss > 1 else False