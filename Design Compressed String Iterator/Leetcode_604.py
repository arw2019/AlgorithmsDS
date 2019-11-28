import re
from collections import deque

class StringIterator:

    def __init__(self, compressedString: str):
        self.encoding = deque(list(filter(lambda c: c, re.findall(r"[^\W\d_]+|\d+", compressedString))))
    
        
    def next(self) -> str:
        if self.hasNext():
            char = self.encoding.popleft()
            num_repeats = self.encoding.popleft()
            if int(num_repeats) > 1: 
                self.encoding.appendleft(str(int(num_repeats)-1))
                self.encoding.appendleft(char)
            return char
        return ' '
        

    def hasNext(self) -> bool:
        return len(self.encoding) != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
