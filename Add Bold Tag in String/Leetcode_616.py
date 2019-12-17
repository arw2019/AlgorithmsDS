# improve speed by storing only boundaries of bold tags
from collections import defaultdict
class Solution:
    def addBoldTag(self, s: str, dictionary: List[str]) -> str:
        if not dictionary or not s: return s
        
        d = defaultdict(list)
        for word in dictionary:
            d[word[0]].append(word)
        mask = []
        for i, char in enumerate(s):
            for word in d[char]:
                wl = len(word)
                if s[i:i+wl] == word:
                    if mask and mask[-1] >= i-1:
                        mask[-1] = max(mask[-1], i+wl-1)
                    else:
                        mask.extend([i,i+wl-1])
        if not mask: return s
        res = [s[:mask[0]]]
        for i in range(0, len(mask), 2):
            res.extend(['<b>',s[mask[i]:mask[i+1]+1],'</b>'])
            if i+2 < len(mask):
                res.append(s[mask[i+1]+1:mask[i+2]])
            else:
                res.append(s[mask[i+1]+1:])
        return ''.join(res)
    
#### correct but relatively slow solution
import re
class Solution:
    def addBoldTag(self, s: str, dictionary: List[str]) -> str:
        mask = [False]*len(s)
        for substring in dictionary:
            for m in re.finditer('(?=' + substring + ')', s):
                for i in range(m.start(), m.start() + len(substring)):
                    mask[i] = True
        res, bold = '', False
        for i, char in enumerate(s):
            if not bold and mask[i]:
                res += '<b>'
                bold = True
            elif bold and not mask[i]:
                res += '</b>'
                bold = False
            res += char
        if bold: res += '</b>'
        return res
