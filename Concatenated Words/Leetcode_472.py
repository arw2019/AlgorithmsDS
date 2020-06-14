class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))
        allWords, concatWords  = set(), set()
        def isConcat(word):
            if word in allWords:
                return True
            for i in range(1, len(word)):
                if isConcat(word[:i]) and isConcat(word[i:]):
                    return True
            
                
        for w in words:
            if isConcat(w): concatWords.add(w)
            else: allWords.add(w)
       
        return list(concatWords)
