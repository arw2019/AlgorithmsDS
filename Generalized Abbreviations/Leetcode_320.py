class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = [""]
        for i, char in enumerate(word):
            newRes = []
            for x in res: 
                if not x or x[-1] != '#': 
                    newRes += [x+char, x+'#1#']
                else: 
                    y, num, _ = x.split('#')
                    newRes += [y+ num + char, y + '#' + str(int(num)+1) + '#']
            res = newRes
        ans = []
        for x in res:
            if not x or x[-1] != '#': 
                ans += [x]
            else:
                y, num, _ = x.split('#')
                ans += [y+num]
        return ans
