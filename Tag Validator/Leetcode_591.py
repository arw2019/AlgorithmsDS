# following the approach of https://leetcode.com/problems/tag-validator/discuss/279586/Python-One-pass-leveraging-State-Machine
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        state = ['plain','open','close','cdata']
        cur = 'plain'
        openTag, closeTag = '', ''
        i = 0
        while i < len(code):
            char = code[i]
            if cur == 'plain':
                if not stack and i != 0:
                    # all plain text must be enclosed by a tag
                    return False
                if code[i:i+9] == "<![CDATA[":
                    cur = 'cdata'
                    i += 9
                    continue
                elif code[i:i+2] == '</':
                    cur = 'close'
                    i += 2
                    continue
                elif char == '<':
                    cur = 'open'
            elif cur == 'open':
                if char == '>':
                    if not 1<=len(openTag)<=9:
                        return False
                    stack.append(openTag)
                    openTag = ''
                    cur = 'plain'
                    i+=1
                    continue
                if not char.isupper():
                    return False
                openTag += char
            elif cur == 'close':
                if char == '>':
                    if not 1<=len(closeTag)<=9:
                        return False
                    if not stack or closeTag != stack[-1]:
                        return False
                    else:
                        stack.pop()
                    closeTag = ''
                    cur = 'plain'
                    i+=1
                    continue
                if not char.isupper():
                    return False
                closeTag += char
            elif cur == 'cdata':
                if code[i:i+3] == ']]>':
                    i+=3
                    cur = 'plain'
                    continue
            i+=1
        
        return False if stack or cur != 'plain' else True
