class Solution(object):
    def removeComments(self, source: List[str]) -> List[str]:
        ans, buffer, blockComment = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                if char == '/' and i+1<len(line) and line[i+1] == '/' and not blockComment:
                    i = len(line)
                elif char == '/' and i+1<len(line) and line[i+1] == '*' and not blockComment:
                    blockComment = True
                    i += 1
                elif char == '*' and i+1<len(line) and line[i+1]=='/' and blockComment:
                    blockComment = False
                    i+=1
                elif not blockComment:
                    buffer += char
                i+=1
            if buffer and not blockComment:
                ans.append(buffer)
                buffer = ''
        return ans
