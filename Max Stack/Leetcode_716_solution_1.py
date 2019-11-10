# top 36%  - while implemention is correct, there is plenty of room to improve efficiency!
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []
        

    def push(self, x: int) -> None:
        if self.stack: self.stack.append((x, max(x, self.peekMax())))
        else: self.stack.append((x, x))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1] if self.stack else None

    def popMax(self) -> int:
        if not self.stack: return None
        stack2 = []
        curMax = self.peekMax()
        while self.stack[-1][1] == curMax:
            x = self.stack.pop()
            if x[0] < curMax: stack2.append(x)
            else: break
        while stack2:
            self.push(stack2.pop()[0])
        return curMax
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
