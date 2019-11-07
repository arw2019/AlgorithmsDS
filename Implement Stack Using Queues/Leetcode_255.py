from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.q1: self.q1.append(x)
        else: self.q2.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not (self.q1 or self.q2):
            return ValueError("empty stack")
        elif self.q1:
            while len(self.q1)>1:
                self.q2.append(self.q1.popleft())
            return self.q1.pop()
        else:
            while len(self.q2)>1:
                self.q1.append(self.q2.popleft())
            return self.q2.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not (self.q1 or self.q2):
            return ValueError("empty stack")
        elif self.q1:
            while len(self.q1)>1:
                self.q2.append(self.q1.popleft())
            val = self.q1.popleft()
            self.q2.append(val)
            return val
        else:
            while len(self.q2)>1:
                self.q1.append(self.q2.popleft())
            val = self.q2.popleft()
            self.q1.append(val)
            return val
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not (self.q1 or self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
