class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.cache = {}
        for w in sorted(words, key=len):
            self.cache[w] = max(self.cache.get(w[:i]+w[i+1:],0) + 1 for i in range(len(w)))
        return max(self.cache.values())
