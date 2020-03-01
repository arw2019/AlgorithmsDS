class Solution:
    def __init__(self):
        self.d = {
            '+': lambda x, y, lastVal: (x+y, y),
            '-': lambda x, y, lastVal: (x-y, -y),
            '*': lambda x, y, lastVal: (x-lastVal+lastVal*y, 
                                                        lastVal*y),
            '/': lambda x, y, lastVal: (x-lastVal+int(lastVal/y),
                                                        int(lastVal/y))
        }
    
    def calculate(self, s: str) -> int:
        stack, res, lastVal = [], 0, 0
        op = '-' if s.lstrip()[0]=='-' else '+'
        i = 0
        while i < len(s):
            curChar = s[i]
            if curChar.isdigit():
                curNum = 0
                while i < len(s) and s[i].isdigit():
                    curNum = curNum*10 + int(s[i])
                    i+=1
                i-=1
                res, lastVal = self.d[op](res, curNum, lastVal)
            elif curChar in self.d:
                op = curChar
            elif curChar == '(':
                for el in (str(res), str(lastVal), str(op)):
                    stack.append(el)
                res, op = 0, '+'
            elif curChar == ')':
                prevOp = stack.pop()
                prevLastVal = int(stack.pop())
                prevRes = int(stack.pop())
                res, lastVal = self.d[prevOp](prevRes, res, prevLastVal)
            elif curChar != ' ':
                print(s[i])
                raise ValueError('Input contains invalid characters.')
            i+=1
       
        
        return  res
