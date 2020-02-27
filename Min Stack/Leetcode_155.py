# version 1

from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.getMin())))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

 # version 2

class MinStack:

    def __init__(self):
        self.stack = []
        self.smallestElements = [float('inf')]

    def push(self, x: int) -> None:
        self.stack += [x]
        self.smallestElements += [min(self.smallestElements[-1], x)]

    def pop(self) -> None:
        self.stack.pop()   
        self.smallestElements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallestElements[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
