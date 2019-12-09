class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        queue = [""]
        for i, char in enumerate(word):
            newQueue = []
            for x in queue: 
                if not x or x[-1] != '#': 
                    newQueue += [x+char, x+'#1#']
                else: 
                    y, num, _ = x.split('#')
                    newQueue += [y+ num + char, y + '#' + str(int(num)+1) + '#']
            queue = newQueue
        ans = []
        for x in queue:
            if not x or x[-1] != '#': 
                ans += [x]
            else:
                y, num, _ = x.split('#')
                ans += [y+num]
        return ans
