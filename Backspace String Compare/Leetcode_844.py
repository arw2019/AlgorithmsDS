# top 3%
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def parse(s: str) -> str:
            res = ''
            for char in s:
                if char == '#':
                    if res: res = res[:-1]
                else:
                    res += char
            return res
        
        return parse(S) == parse(T)