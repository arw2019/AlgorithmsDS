# O(N^2) space solution
# but 4 times faster on LC
from collections import defaultdict
class WordFilter:

    def __init__(self, words: List[str]):
        d = {word: weight for weight, word in enumerate(words)}
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        for word, weight in d.items():
            for i in range(len(word)+1):
                self.prefixes[word[:i]].add(weight)
                self.suffixes[word[i:]].add(weight)

    def f(self, prefix: str, suffix: str) -> int:
        candidates = self.prefixes[prefix] & self.suffixes[suffix]
        return max(candidates) if candidates else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)