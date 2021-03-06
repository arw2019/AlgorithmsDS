from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
       
        @lru_cache() 
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            return False
        
        return [word for word in words if dfs(word)]
    
######

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
