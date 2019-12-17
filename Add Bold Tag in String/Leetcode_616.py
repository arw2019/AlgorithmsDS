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
