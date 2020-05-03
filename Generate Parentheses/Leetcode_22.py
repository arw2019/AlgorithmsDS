from functools import lru_cache
class Solution:
    @lru_cache()
    def generateParenthesis(self, n: int) -> List[str]:    
        if n == 0: return ['']
        if n == 1: return ['()']
        res = []
        for i in range(1, n):
            s1, s2 = map(self.generateParenthesis, [i, n-1-i])
            for p1 in s1:
                for p2 in s2:
                    res += ['()' + p1 + p2] + [p1 + '()' + p2] + [p1 + p2 + '()']
                    res += ['(' + p1 + ')' + p2] + [p1 + '(' + p2 + ')']
                    res += ['(' + p1 + p2 + ')']
        
        return list(set(res))
