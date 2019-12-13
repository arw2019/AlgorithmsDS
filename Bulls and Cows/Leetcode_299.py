from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls, cows = 0, 0
        
        s, g = defaultdict(set), defaultdict(set)
        for i, char in enumerate(secret):
            s[char].add(i)
        for i, char in enumerate(guess):
            g[char].add(i)
        
        for char, idxs in s.items():
            bulls_char = len(s[char] & g[char])
            bulls += bulls_char
            cows += max(0, min(len(s[char]), len(g[char])) - bulls_char)
        
        return str(bulls) + 'A' + str(cows) + 'B'
