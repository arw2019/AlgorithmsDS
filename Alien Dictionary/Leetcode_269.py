 
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        N = len(words)
        less = []
        for i in range(N-1):
            word1, word2 = words[i], words[i+1]
            scan_length = min(len(word1), len(word2))
            for j in range(scan_length):
                char1, char2 = word1[j], word2[j]
                if char1 != char2:
                    less += [char1 + char2]
                    break
      
                    
        chars = set(''.join(words))
        order = []
        if (not less and 
            any(len(words[i+1]) < len(words[i]) for i in range(N-1))): return ''
        while less:
            free = chars - {pair[1] for pair in less}
            if not free: return ''
            order += free
            chars -= free
            less = [pair for pair in less if free.isdisjoint(pair)]
      
        return ''.join(order + list(chars))
