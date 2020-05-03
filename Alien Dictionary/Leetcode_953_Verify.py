# same algo with early stopping
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char: i for i, char in enumerate(order)}
        def isGreater(w1: str, w2: str) -> bool:
            key = lambda word: [d[char] for char in word]
            return key(w1) > key(w2)
        return all(isGreater(words[i+1], words[i]) for i in range(len(words)-1))

# lighter implementation of same idea
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char: i for i, char in enumerate(order)}
        wordsAlienOrder = sorted(words, key=lambda word: [d[char] for char in word]) 
        return words == wordsAlienOrder
    
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        aliendict = {letter: priority for priority, letter in enumerate(order)}
        english = list("abcdefghijklmnopqrstuvwxyz") 
        def toEnglish(word: str):
            return ''.join([english[aliendict[char]] for char in word])
        return sorted(words, key=lambda w: toEnglish(w)) == words
