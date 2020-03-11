from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        chars= sorted(cnt.keys())
        res = []
        
        while len(res) < len(s):
            i=0
            while i<len(chars) and cnt[chars[i]] == 0: i+=1
            
            for char in chars[i:]:
                if cnt[char] > 0:
                    res += [char]
                    cnt[char] -= 1
                    
            i = len(chars)-1
            while i>0 and cnt[chars[i]] == 0: i-=1
            
            for char in reversed(chars[:i+1]):
                if cnt[char] > 0:
                    res += [char]
                    cnt[char] -= 1
      
        return ''.join(res)
    
