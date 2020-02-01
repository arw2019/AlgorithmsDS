class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        flag = True if s[-1] !='#' else False
        ss = s.split('#')
        for i, x in enumerate(ss):
            if i == len(ss) - 1 and flag:
                res += ''.join(chr(ord('a') + int(y) - 1) for y in x)  
            elif x and int(x) <= 26:
                res += chr(ord('a') + int(x) - 1)
            elif x:
                while int(x) > 26:
                    res += chr(ord('a') + int(x[0]) - 1)
                    x = x[1:]
                else:
                    res += chr(ord('a') + int(x) - 1)
        return res
