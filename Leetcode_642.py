#correct but not efficient enough for LC acceptance

import string

class TrieNode(object):
    def __init__(self):
        self.hotDegree = 0
        self.children = collections.defaultdict(TrieNode)
            
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        
        self.root = TrieNode()
        for sentence, hotDegree in zip(sentences, times):
            self._insert(sentence, hotDegree)
            
        self.asciiDict = {char: i for i, char in enumerate(string.ascii_letters)}
        self.asciiDict[' '] = -1
        
        self._reset()
        
    def _reset(self):
        self.cur = self.root
        self.soFar = ''
        self.res = []
        
    def _insert(self, sentence: str, hotDegree: int = 1) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in sentence:
            node = node.children[c]
        node.hotDegree += hotDegree
        
        
    def _findAll(self, node: 'TrieNode' = None, text: str = '') -> None:
        node = node or self.cur
        if not node: return
        if node.hotDegree:
            self.res.append((text, node.hotDegree))
        for char in string.ascii_letters + ' ':
            if char in node.children:
                self._findAll(node.children[char], text+char)
    
    def _ascii_key(self, text):
        return [self.asciiDict[char] for char in text] 
    
    def input(self, c: str) -> List[str]:
        
        if c == '#':
            if self.soFar:
                self._insert(self.soFar)
            self._reset()
            return
        
        if not self.cur and c in self.asciiDict:
            return []
            
        self.res = []
        self.cur = self.cur.children[c]
        self.soFar += c
        self._findAll()
        if not self.res: 
            return []
        self.res.sort(key=lambda x: (-x[1], self._ascii_key(x[0])))
        if len(self.res) > 3: self.res = self.res[:3]
        return [self.soFar+x[0] for x in self.res]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
