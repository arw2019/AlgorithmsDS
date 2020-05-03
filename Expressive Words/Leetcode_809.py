class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def getEncoding(word: str):
            out = []
            for char in word:
                if not out or char != out[-1][0]:
                    out += [[char, 1]]
                else:
                    out[-1][1] += 1
            return out
        
        ans = 0
        ref = getEncoding(S)
        for word in words:
            cur = getEncoding(word)
            isStretchy = True
            if len(ref) != len(cur): 
                isStretchy = False
                continue
            for i in range(len(ref)):
                charRef, numRef = ref[i]
                charCur, numCur = cur[i]
                if charRef != charCur:
                    isStretchy = False
                elif numRef != numCur and (numRef < 3 or numRef < numCur):
                    isStretchy = False
            if isStretchy:
                ans += 1
       
        return ans
