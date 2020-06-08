class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, numOfLetters = [], [], 0
        for w in words:
            if numOfLetters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth-numOfLetters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, numOfLetters = [], 0
            cur += [w]
            numOfLetters += len(w)
        return res+[' '.join(cur).ljust(maxWidth)]
