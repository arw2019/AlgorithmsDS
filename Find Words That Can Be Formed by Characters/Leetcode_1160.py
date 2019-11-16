# top 0.02 %
from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = defaultdict(int)
        for char in set(chars):
            d[char] = chars.count(char)
        ans = 0
        for word in words:
            valid = True
            for char in word:
                if word.count(char) > d[char]:
                    valid = False
                    break
                    # this part saves a lot of time
                    # once we find that the word is invalid we stop
            if valid:
                ans += len(word)
        return ans
