# top 2%
class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{',']':'['}
        stack = []
        i = 0
        while i < len(s):
            if s[i] in d.values():
                stack.append(s[i])
            elif stack:
                if stack[-1] != d[s[i]]:
                    return False
                else:
                    del stack[-1]
            else:
                return False
            i+=1
        return not stack                
