from collections import defaultdict, deque

class TrieNode(object):
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.weight = 0

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.preRoot = TrieNode()
        self.suffRoot = TrieNode()
        for i, word in enumerate(words):
            self._insert(word, i)
        
    def _insert(self, word: str, w: int) -> None:
        """insert a word with weight w into the prefix and suffix trees"""
        cur = self.preRoot
        for char in word:
            cur = cur.links[char]
        cur.weight = max(cur.weight, w)
        
        cur = self.suffRoot
        for char in word[::-1]:
            cur = cur.links[char]
        cur.weight = max(cur.weight, w)
    
    def _allWeights(self, link: TrieNode) -> List[int]:
        res = [link.weight]
        for char, node in link.links.items():
            res += self._allWeights(node)
        return res
    
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.preRoot
        for char in prefix: 
            if char not in cur.links: 
                return -1
            cur = cur.links[char]
        prefixWeights = self._allWeights(cur)
        
        cur = self.suffRoot
        for char in suffix[::-1]: 
            if char not in cur.links: 
                return -1
            cur = cur.links[char]
        suffixWeights = self._allWeights(cur)
        
        validWords = set(prefixWeights).intersection(set(suffixWeights))
        return sorted(validWords, reverse=True)[0] if validWords else -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)