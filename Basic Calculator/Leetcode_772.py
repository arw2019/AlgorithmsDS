class Solution:
    
    def __init__(self):
        self.d = {
            '+': lambda res, curVal, lastVal: (res+curVal, curVal),
            '-': lambda res, curVal, lastVal: (res-curVal, -curVal),
            '*': lambda res, curVal, lastVal: (res-lastVal+lastVal*curVal, lastVal*curVal),
            '/': lambda res, curVal, lastVal: (res-lastVal+int(lastVal/curVal), int(lastVal/curVal)),
                
        }
    
    def calculate(self, s: str) -> int:
        stack, res, lastVal = [], 0, 0
        op = '-' if s.lstrip()[0]=='-' else '+'
        i = 0
        while i<len(s):
            curChar=s[i]
            if curChar.isdigit():
                curNum = 0
                while i<len(s) and s[i].isdigit():
                    curNum = 10*curNum + int(s[i])
                    i+=1
                i-=1
                res, lastVal = self.d[op](res, curNum, lastVal)
            elif curChar in self.d:
                op = curChar
            elif curChar=='(':
                for el in (res, lastVal, op):
                    stack += [el]
                res, op = 0, '+'
            elif curChar == ')':
                prevOp = stack.pop()
                prevLastVal = stack.pop()
                prevRes = stack.pop()
                res, lastVal = self.d[prevOp](prevRes, res, prevLastVal)
            elif curChar != ' ':
                raise ValueError(f's[i] is not a valid character.')
            i+=1
        return res
