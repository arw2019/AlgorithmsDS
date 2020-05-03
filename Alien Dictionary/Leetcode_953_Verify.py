class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        aliendict = {letter: priority for priority, letter in enumerate(order)}
        english = list("abcdefghijklmnopqrstuvwxyz") 
        def toEnglish(word: str):
            return ''.join([english[aliendict[char]] for char in word])
        return sorted(words, key=lambda w: toEnglish(w)) == words

# lighter implementation of same idea
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char: i for i, char in enumerate(order)}
        wordsAlienOrder = sorted(words, key=lambda word: [d[char] for char in word]) 
        return words == wordsAlienOrder
