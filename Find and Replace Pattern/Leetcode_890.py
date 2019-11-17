# top 0.25%

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def isMatch(word: str, pattern: str) -> bool:
            w, p = {}, {}
            for i in range(len(pattern)):
                x, px = word[i], pattern[i]
                if x not in w and px not in p:
                    w[x], p[px] = px, x
                elif x in w and px in p and w[x]==px and p[px]==x:
                    continue
                else:
                    return False
            return True       
        
        return [word for word in words if isMatch(word, pattern)]
