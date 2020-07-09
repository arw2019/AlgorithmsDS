class Solution:
    def alienOrder(self, words: List[str]) -> str:
        N = len(words)
        less = []
        
        for i in range(N-1):
            word1, word2 = words[i:i+2]
            
            scan_length = min(
                len(word1), 
                len(word2)
            )
            
            less += next(
                (
                    [word1[j]+word2[j]]
                    for j in range(scan_length)
                    if word1[j] != word2[j]
                ),
            []
            )
                    
        chars = set(''.join(words))
        order = []
        
        if not less and any(
            len(words[i+1])<len(words[i]) 
            for i in range(N-1)
        ):
            return ''
        
        while less:
            free = chars - {char for _, char in less}
            if not free: return ''
            order += free
            chars -= free
            less = [
                pair 
                for pair in less 
                if free.isdisjoint(pair)
            ]
            
        return ''.join(order + list(chars))
