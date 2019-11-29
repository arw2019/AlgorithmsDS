# substring search with string.find() method
# top 0.1%

class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        mask = [0]*len(S)
        for w in words:
            start = S.find(w, 0)
            while start != -1:
                mask[start: start + len(w)] = [1] * len(w)
                start = S.find(w, start + 1)

        res, bold = '', False
        for i, char in enumerate(S):
            if mask[i] == 0:
                if bold: 
                    res += '</b>'
                    bold = False
            else: # mask[i] == 1
                if not bold:
                    res += '<b>'
                    bold = True
            res += char
        if bold: res += '</b>'
        return res

# substring search with regex
# top 50% (108ms)
import re
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        mask = [0]*len(S)
        for w in words:
            for m in re.finditer('(?='+w+')', S):
                # print(w, m.start(), m.start() + len(w))
                for i in range(m.start(),  m.start() + len(w)):
                    mask[i] = 1
        # print(mask)
        res, bold = '', False
        for i, char in enumerate(S):
            if mask[i] == 0:
                if bold: 
                    res += '</b>'
                    bold = False
            else: # mask[i] == 1
                if not bold:
                    res += '<b>'
                    bold = True
            res += char
        if bold: res += '</b>'
        return res