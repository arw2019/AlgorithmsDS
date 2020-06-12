# same algorithm, nimbler implementation

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
            
        print(trie) 
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    


# first try

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
