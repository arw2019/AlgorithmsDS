from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.isWord = False # set to True when trie ends

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        cur = self.root
        for char in word:
            cur = cur.links[char]
        cur.isWord = True
        
    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        cur = self.root
        for char in word:
            if char not in cur.links: return False
            cur = cur.links[char]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            if char not in cur.links: return False
            cur = cur.links[char]       
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)