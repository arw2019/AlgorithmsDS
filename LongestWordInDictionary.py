class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        ans, maxlen = [], 0
        for word in words:
            if len(word) < maxlen: continue
            valid = True
            for i in range(1,len(word)+1):
                if word[:i] not in s: 
                    valid = False
                    break
            if valid:
                if len(word) == maxlen: ans.append(word)
                elif len(word) > maxlen: ans, maxlen = [word], len(word)
        
        return '' if maxlen==0 else sorted(ans)[0]
