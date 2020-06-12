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

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res, trie = set(), Trie()
        [trie.insert(w) for w in words]
        def dfs(i, j, word='', seen=set()):
            nonlocal res
            if (i,j) not in seen and 0<=i<m and 0<=j<n and (not word or trie.startsWith(word)):
                seen.add((i,j))
                word+=board[i][j]
                if trie.search(word): res.add(word)
                dfs(i-1, j, word)
                dfs(i+1, j, word)
                dfs(i, j-1, word)
                dfs(i, j+1, word)
                seen.remove((i,j))
        [dfs(i, j) for i in range(m) for j in range(n)]
        return list(res)
