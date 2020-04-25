from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack, cnt = [], defaultdict(int)
        N = len(formula)
        i = 0
        depth = 0
        while i < N:
            if formula[i].isupper():
                char = formula[i]
                i+=1
                while i<N and formula[i].islower():
                    char += formula[i]
                    i += 1    
                if not (i<N and formula[i].isdigit()):
                    cnt[char] += 1
                else:
                    stack += [char] + [1] 
            elif formula[i].isdigit():
                num = ''
                while i < N and formula[i].isdigit():
                    num += formula[i]
                    i += 1
                stack[-1] = int(num)
                if not depth:
                    cnt[char] += int(num)
                    stack.pop(), stack.pop()
                else:
                    stack += [char] + [num]
            elif formula == '(':
                pass
            elif formula == ')':
                pass
        
        res = []
        for element, count in sorted(cnt.items()):
            res += element + str(count)
        return ''.join(res)
