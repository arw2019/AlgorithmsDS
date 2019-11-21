# top 3%
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        ans = float('inf')
        for char in ['b', 'a','n']:
            ans = min(ans, c[char])
        for char in ['l', 'o']:
            ans = min(ans, c[char]//2)
        return ans
